import jieba
f = open('article.txt', 'r', encoding='utf-8')
txt = f.read()
words = jieba.lcut(txt)
f.close()

counts = {}
for w in words:
    if w in counts:
        counts[w] = counts[w] + 1
    else:
        counts[w] = 1
print(counts)