import jieba

f1 = open('散文.txt', 'r', encoding='utf-8')
text1 = f1.read()
f1.close()
words = jieba.lcut(text1)

f2 = open('城市.txt', 'r', encoding='utf-8')
text2 = f2.read()
f2.close()
names = text2.split()

cities = []
# 遍历列表 words
for i in words:
    if a in names:
    # 如果词语是城市,就将它添加到列表 cities 中
    cities.append(a)


print(cities)
