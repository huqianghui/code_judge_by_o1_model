import jieba
f = open('article.txt', 'r', encoding='utf-8')
txt = f.read()
words = jieba.lcut(txt)
f.close()
c={}
for w in words:
    b=c.get(w,0)
    c[w]=b+1
print(c)