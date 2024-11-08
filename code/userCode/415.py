f = open('抹香鲸.txt', 'r', encoding='utf-8')
s = f.read()
f.close()
print('原文件内容为:\n' + s)
f = open('抹香鲸.txt', 'w', encoding='utf-8')
# 使用写入模式打开文件 '抹香鲸.txt'
f.write( '哺乳纲抹香鲸科')
# 写入正确信息 '哺乳纲抹香鲸科'
f.close()
# 关闭文件


f = open('抹香鲸.txt', 'r', encoding='utf-8')
s = f.read()
f.close()
print('新文件内容为:\n' + s)