f = open('中国.txt', 'r', encoding='utf-8')
s = f.read()
f.close()
a = s.split(',')

cn = [int(i) for i in a]

print(cn)