from PIL import Image
import wordcloud
import jieba

f = open('少年中国说.txt', 'r', encoding='utf-8')
text = f.read()
f.close()

lst = jieba.lcut(text)
m = ' '.join(lst)

print('开始制作词云...')
s = {'智则', '富则', '强则', '而全'}
mac = 'PingFang.ttc'
win = 'simhei.ttf'
w = wordcloud.WordCloud(
    width=1000,
    height=700,
    # 填写自己电脑系统字体，此处以Windows电脑为例
    font_path=win,
    stopwords=s
)
w.generate(m)
w.to_file('词云2.png')


print('词云图片已生成，开始展示图片')

p = Image.open('词云2.png')
p.show()
print('图片展示完成')