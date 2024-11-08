# 打开 '散文.txt' 文件
f = open('散文.txt', 'r', encoding='utf-8')
# 读取文件内容
text = f.read()
# 关闭文件
f.close()

print('散文集中一共有', len(text), '字')