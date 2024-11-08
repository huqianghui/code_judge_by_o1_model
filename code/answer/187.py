import jieba

f = open('散文.txt', 'r', encoding='utf-8')
text = f.read()
f.close()

# 使用lcut()函数对读取到的内容进行分词
words = jieba.lcut(text)

print('一共出现了', len(words), '个词语')