# 导入jieba库
import jieba
f = open('梦幻奇旅.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()

linewords = []
# 遍历存储文章内容的列表, 逐行分词, 并把分词结果存储到linewords中.
for i in lines:
    word = jieba.lcut(i)
    linewords.append(word)
print(linewords)