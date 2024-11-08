from PIL import Image
import wordcloud
import jieba

f = open('散文.txt', 'r', encoding='utf-8')
text = f.read()
f.close()

words = jieba.lcut(text)
s = ' '.join(words)

print('开始绘制词云...')
mac = 'PingFang.ttc'
win = 'simhei.ttf'

sw = {'我们', '他们', '没有', '一个', '就是', '因为', '所以', '然而'}

w = wordcloud.WordCloud(
    width=300,
    height=300,
    background_color='white',
    collocations=False,
    stopwords=sw,
    # 根据自己的电脑系统选择中文字体
    font_path=win
)

# 加载词云文本
w.generate(s)
w.to_file('词云.png')

print('词云图片已生成，开始展示图片')
p = Image.open('词云.png')
p.show()
print('图片展示完成')