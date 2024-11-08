import jieba
f = open('article.txt', 'r', encoding='utf-8')
txt = f.read()
words = jieba.lcut(txt)
f.close()

a = '程序'
c = 0
for w in words:
    if w == a:
        c += 1
print(a, c)