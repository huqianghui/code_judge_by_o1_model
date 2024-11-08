from PIL import Image
import wordcloud

text = '生日快乐 HappyBirthday'

wc = wordcloud.WordCloud(
    font_path='FZY4JW.TTF',
    width=800,
    height=600,
    background_color='white',
    repeat=True
)
wc.generate(text)
wc.to_file('海报.png')

p = Image.open('海报.png')
p.show()