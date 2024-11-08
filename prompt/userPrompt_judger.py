from langchain_core.prompts import (
    HumanMessagePromptTemplate,
)

userPromptTemplateJudger = '''
# LLM1
${LLM1_result}
'''

user_prompt_judger = HumanMessagePromptTemplate.from_template(userPromptTemplateJudger)