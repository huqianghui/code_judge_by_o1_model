from PIL import Image
import wordcloud

text = '生日快乐 HappyBirthday'

# 1. 创建词云对象
wc = wordcloud.WordCloud()
# 2. 加载词云文本
# 在此处编写代码, 利用文本text生成词云图
词云对象.generate(词云文本)

# 3. 保存词云图片
wc.to_file('海报.png')

p = Image.open('海报.png')
p.show()