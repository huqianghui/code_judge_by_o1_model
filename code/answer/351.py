import jieba
f = open('article.txt', 'r', encoding='utf-8')
txt = f.read()
words = jieba.lcut(txt)
f.close()

counts = {}
for w in words:
    if len(w) > 1:  
        c = counts.get(w, 0)
        counts[w] = c + 1

m = 0
k = 0
for c in counts:
    if counts[c] > m:
        m = counts[c]
        k = c
print(k, counts[k])
