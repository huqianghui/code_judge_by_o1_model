from PIL import Image
import wordcloud
import numpy

text = '生日快乐 HappyBirthday'

image = Image.open('photo.jpg')
img = numpy.array(image)
# 使用wordcloud库中的颜色生成器ImageColorGenerator() 生成字体需要的颜色
image_color=wordcloud.ImageColorGenerator(img)

wc = wordcloud.WordCloud(
    font_path='FZY4JW.TTF',
    background_color='white',
    repeat=True,
    mask=img,
    # 把颜色结果赋值给color_func参数
    color_func=image_color
)
wc.generate(text)
wc.to_file('海报.png')

p = Image.open('海报.png')
p.show()