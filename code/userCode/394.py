from PIL import Image
import wordcloud
import jieba

f = open('少年中国说.txt', 'r', encoding='utf-8')
text = f.read()
f.close()

lst = jieba.lcut(text)
m = ' '.join(lst)

print('开始制作词云...')
# 将自定义的停用词存放在集合s中
s = {            }
mac = 'PingFang.ttc'
win = 'simhei.ttf'
w = wordcloud.WordCloud(
    width=1000,
    height=700,
    # 根据自己的电脑系统选择中文字体
    font_path=    ,
    # 将自定义停用词集合赋值给stopwords
    stopwords=
)
w.generate(m)
w.to_file('词云2.png')


print('词云图片已生成,开始展示图片')

p = Image.open('词云2.png')
p.show()
print('图片展示完成')