from langchain_core.prompts import (
    HumanMessagePromptTemplate,
)

userPromptTemplateCodeModify = '''
# Correct Answer
``` python
${answer}
```

# User Code
``` python
${user_code}
'''

user_prompt_code_modify = HumanMessagePromptTemplate.from_template(userPromptTemplateCodeModify)