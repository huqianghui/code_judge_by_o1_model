f = open('抹香鲸.txt', 'r', encoding='utf-8')
s = f.read()
f.close()
print('原文件内容为:\n' + s)

# 使用写入模式打开文件 '抹香鲸.txt'
f = open('抹香鲸.txt', 'w', encoding='utf-8')
# 写入正确信息 '哺乳纲抹香鲸科'
f.write('哺乳纲抹香鲸科')
# 关闭文件
f.close()

f = open('抹香鲸.txt', 'r', encoding='utf-8')
s = f.read()
f.close()
print('新文件内容为:\n' + s)