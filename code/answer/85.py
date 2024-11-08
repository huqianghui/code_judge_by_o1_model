# 使用追加模式打开 '海岛动物.txt' 文件
f = open('海岛动物.txt', 'a', encoding='utf-8')
# 追加动物名称 '海鸥'
f.write('海鸥')
f.close()

f = open('海岛动物.txt', 'r', encoding='utf-8')
s = f.read()
f.close()
print(s)