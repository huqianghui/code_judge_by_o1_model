from PIL import Image
import wordcloud

text = '生日快乐 HappyBirthday'

wc = wordcloud.WordCloud()
wc.generate(text)
wc.to_file('海报.png')

p = Image.open('海报.png')
p.show()