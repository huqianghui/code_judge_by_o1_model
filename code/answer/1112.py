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
for w in words:
    if w in names:
        cities.append(w)

counts = {}
# 遍历列表 cities
for w in cities:
    # 如果词语在字典中,就将对应的出现次数增加1;否则,就将对应的出现次数设置为1
    if w in counts:
        counts[w] += 1
    else:
        counts[w] = 1

print(counts)