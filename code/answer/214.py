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
row = search(lines, w)
print(w, '出现在第', row, '行')