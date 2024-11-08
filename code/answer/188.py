from PIL import Image
import wordcloud
import numpy

text = '生日快乐 HappyBirthday'

image = Image.open('photo.jpg')
img = numpy.array(image)
image_color = wordcloud.ImageColorGenerator(img)

wc = wordcloud.WordCloud(
    font_path='FZY4JW.TTF',
    background_color='white',
    repeat=True,
    mask=img,
    contour_width=2,
    contour_color='grey',
    color_func=image_color
)
wc.generate(text)
wc.to_file('海报.png')

p = Image.open('海报.png')
p.show()