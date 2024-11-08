# 正确答案
``` python
${answer}
```

# 用户代码
``` python
${user_code}
```

``` python
def add_line_numbers(code):
    """用户代码增加行号
    """
    lines = code.split("\n")
    numbered_lines = [f"第{i + 1}行: {line}" for i, line in enumerate(lines)]
    return "\n".join(numbered_lines)
def remove_empty_lines(text):
    """用户代码、正确答案移除空白行
    """
    lines = [line for line in text.split("\n") if line.strip()]
    return "\n".join(lines)
```