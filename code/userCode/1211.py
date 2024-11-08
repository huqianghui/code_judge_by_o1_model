'''
函数search()
功能: 查找词语出现在第几行
参数: text-存储文件内容的列表; word-查找的词语
返回值: 词语所在的行号
'''
def search(text, word):
    for i in range(len(text)):
        if word in text[i]:
            return i + 1

f = open('梦幻奇旅.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()

for i in range(len(lines)):
    print(i + 1, lines[i])

w = input()
# 在这里编写代码
row = search(lines,w)
print(w, '出现在第', row, '行')


