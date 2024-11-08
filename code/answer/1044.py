import jieba

def search(wordlist, word):
    res = []
    for i in range(len(wordlist)):
        if word in wordlist[i]:
            res.append(i + 1)
    return res

f = open('梦幻奇旅.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()

for i in range(len(lines)):
    print(i + 1, lines[i])

linewords = []
for i in lines:
    words = jieba.lcut(i)
    linewords.append(words)

w = input()
rows = search(linewords, w)
print(w, '出现在', rows, '行')