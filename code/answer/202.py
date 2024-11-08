import jieba

f = open('梦幻奇旅.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()

linewords = []
for i in lines:
    words = jieba.lcut(i)
    linewords.append(words)

print(linewords)