f1 = open('植物名.txt', 'r', encoding='utf-8')
s1 = f1.read()
f1.close()
name = s1.split('-')

f2 = open('科名.txt', 'r', encoding='utf-8')
s2 = f2.read()
f2.close()
family = s2.split('+')

for i in range(5):
    # 将植物名称和科名配对打印出来
    print( name[i]+'属于'+family[i])