import jieba
f = open('article.txt', 'r', encoding='utf-8')
txt = f.read()
words = jieba.lcut(txt)
f.close()

counts = {}
for w in words:
    #使用get()函数完成词语个数统计
    s=counts.get(w,0)
counts[w] = c+1
print(counts)   