import pandas as pd
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from prompt.systemPrompt_EN_codeModify import systemTemplateCodeModify
from prompt.userPrompt_EN_codeModify import user_prompt_code_modify
import asyncio
from roundRobin.azureOpenAIClientRoundRobin import client_manager
import logging
from cache.cacheConfig import cache,async_diskcache
from promptflow.tracing import start_trace,trace
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)


ERROR_CODE="ERR_101: \n"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()

azureOpenAIClient = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)

@async_diskcache("judge_code_by_o1_preivew_moddel")
@retry(wait=wait_random_exponential(multiplier=1, max=60), stop=stop_after_attempt(3))
async def judge_code_by_o1_preivew_moddel(useCode:str,answer:str,index:int):
    user_prompt_code_modify_content = user_prompt_code_modify.format(user_code=useCode, answer=answer)
    aAzureOpenclient = await client_manager.get_next_client()
    # "Unsupported value: 'messages[0].role' does not support 'system' with this model.
    try:
        response = await aAzureOpenclient.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_O1_DEPLOYMENT_NAME","o1-preview"),
            messages=[
            {
                "role": "user",
                "content": systemTemplateCodeModify
            },
            {
                "role": "user",
                "content": str(user_prompt_code_modify_content)
            }]
        )
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"API request failed for row {index + 1}: {e}. Retrying...")
        raise e

@async_diskcache("judge_code_by_o1_mini_moddel")
@retry(wait=wait_random_exponential(multiplier=1, max=60), stop=stop_after_attempt(3))
async def judge_code_by_o1_mini_moddel(useCode:str,answer:str,index:int):
    user_prompt_code_modify_content = user_prompt_code_modify.format(user_code=useCode, answer=answer)
    aAzureOpenclient = await client_manager.get_next_client()
    try:
        response = await aAzureOpenclient.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_O1_MINI_DEPLOYMENT_NAME","o1-mini"),
            messages=[
            {
                "role": "user",
                "content": systemTemplateCodeModify
            },
            {
                "role": "user",
                "content": str(user_prompt_code_modify_content)
            }]
        )
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"{ERROR_CODE} >> API request failed for row {index + 1}: {e}. Retrying...")
        raise e

# Function to process a single row
async def process_row(index, row, semaphore):
    async with semaphore:
        logging.info(f"Processing row {index + 1}")
        user_code = row['user_code']
        answer = row['answer']
        filename = f"{index + 1}.py"

        try:
            o1PreivewModifyResult = await judge_code_by_o1_preivew_moddel(user_code, answer,index)

        except Exception as e:
            logging.error(f"finlly failed to judge_code_by_o1_preivew_moddel for row {index + 1}: {e}")
            o1PreivewModifyResult = f"{ERROR_CODE} row No. : {index + 1} >> {e}"
        
        try:
            o1miniModifyResult = await judge_code_by_o1_mini_moddel(user_code, answer,index)
        except Exception as e:
            logging.error(f"finlly failed to judge_code_by_o1_mini_moddel for row {index + 1}: {e}")
            o1miniModifyResult = f"{ERROR_CODE} row No. : {index + 1} >> {e}"

        try:            
            # Save user_code
            with open(os.path.join('code/userCode', filename), 'w', encoding='utf-8') as f:
                f.write(user_code)

            # Save answer
            with open(os.path.join('code/answer', filename), 'w', encoding='utf-8') as f:
                f.write(answer)
        except Exception as e:
            logging.error(f"Failed to save code files for row {index + 1}: {e}")
        
        return index, o1PreivewModifyResult, o1miniModifyResult

async def read_bad_case_excel_file():
    # Read the Excel file
    df = pd.read_excel(os.getenv("CODE_BAD_CASES_FILE_PATH","docs/azure_badcase_20241028.xlsx"))

    # Create directories if they don't exist
    os.makedirs(os.getenv("CODE_USE_CODE_DIR_PATH","code/userCode"), exist_ok=True)
    os.makedirs(os.getenv("CODE_ANSWER_DIR_PATH","code/answer"), exist_ok=True)
    os.makedirs(os.getenv("RESULT_OUTPUT_DIR_PATH","output"), exist_ok=True)

    o1PreivewOutputs = [None] * len(df)
    o1miniOutputs = [None] * len(df)

    semaphore = asyncio.Semaphore(int(os.getenv("CONCURRENT_TASK_SEMAPHORE_COUNT",140)))  # Limit to 140 concurrent tasks
    tasks = []
    for index, row in df.iterrows():
        tasks.append(process_row(index, row, semaphore))
    
    # Run tasks concurrently
    results = await asyncio.gather(*tasks)

    for index, o1PreivewModifyResult, o1miniModifyResult in results:
        o1PreivewOutputs[index] = o1PreivewModifyResult
        o1miniOutputs[index] = o1miniModifyResult

    df['o1-preview'] = o1PreivewOutputs
    df['o1-mini'] = o1miniOutputs
    output_file_path = os.getenv("RESULT_OUTPUT_DIR_PATH","output") + "/" + "azure_badcase_20241028_updated_withO1_EN_Prompt.xlsx"
    logging.info(f"All rows processed. Saving to Excel file, {output_file_path}")
    df.to_excel(output_file_path, index=False)

    return output_file_path
        
if __name__ == "__main__":
   start_trace()
   result = asyncio.run(read_bad_case_excel_file())

   # Access cache statistics
   hits = cache.hits
   misses = cache.misses
   total_requests = hits + misses

   # Calculate hit and miss rates
   if total_requests > 0:
        hit_rate = hits / total_requests
        miss_rate = misses / total_requests
        print(f"Cache Hits: {hits}")
        print(f"Cache Misses: {misses}")
        print(f"Cache Hit Rate: {hit_rate * 100:.2f}%")
        print(f"Cache Miss Rate: {miss_rate * 100:.2f}%")
   else:
        print("No cache requests have been made.")

   print("save to :",result)
