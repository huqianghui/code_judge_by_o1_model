import jieba
from matplotlib import pyplot

pyplot.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'simhei']

f1 = open('散文.txt', 'r', encoding='utf-8')
text1 = f1.read()
f1.close()
words = jieba.lcut(text1)

f2 = open('城市.txt', 'r', encoding='utf-8')
text2 = f2.read()
f2.close()
names = text2.split()

cities = []
for w in words:
    if w in names:
        cities.append(w)

counts = {}
for w in cities:
    if w in counts:
        counts[w] += 1
    else:
        counts[w] = 1

# 准备数据:x轴数据为字典的key,y轴数据为字典的value
c = list(counts.keys())
n = list(counts.values())
# 绘制柱状图
pyplot.bar(c, n)

pyplot.title('城市出现次数')
print('柱状图绘制中...')
pyplot.show()