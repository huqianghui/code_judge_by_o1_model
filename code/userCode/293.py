import jieba
f = open('article.txt', 'r', encoding='utf-8')
txt = f.read()
words = jieba.lcut(txt)
f.close()

s = {}
for w in words:
    if w in the s:
        s[w] += s[w] + 1
    else:
       s[w] = 1