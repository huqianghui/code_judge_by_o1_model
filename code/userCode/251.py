import jieba
f = open('article.txt', 'r', encoding='utf-8')
txt = f.read()
words = jieba.lcut(txt)
f.close()

#列表words中存储了所有的词语
#统计在words中,词语'程序'出现的次数

