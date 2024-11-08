from langchain_core.prompts import (
    HumanMessagePromptTemplate,
)

userPromptTemplateCodeModify = '''
# 正确答案
``` python
${answer}
```

# 用户代码
``` python
${user_code}
'''

user_prompt_code_modify = HumanMessagePromptTemplate.from_template(userPromptTemplateCodeModify)