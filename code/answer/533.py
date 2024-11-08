from PIL import Image
import wordcloud

text = 'Word Cloud, or Tag Cloud is a visual representation of text data. Word Cloud could display a list of words. The size and color of each word in a Word Cloud indicates its frequency or importance in the text. In another word, significant textual data points can be highlighted using a Word Cloud. It is easy to generate a Word Cloud with Python. You simply need a library called wordcloud. After this class, you will be able to generate a beautiful Word Cloud.'

print('开始绘制词云...')

w = wordcloud.WordCloud(
    width=1000,
    height=600
)
w.generate(text)
w.to_file('词云1.png')

print('词云图片已生成，开始展示图片')


p = Image.open('词云1.png')
p.show()
print('图片展示完成')
