names = ['文件1.txt', '文件2.txt', '文件3.txt', '文件4.txt', '文件5.txt', '文件6.txt', '文件7.txt', '文件8.txt', '文件9.txt']

for name in names:
    f = open(name, 'r', encoding='utf-8')
    # 使用read()命令读取文件内容, 读取后需关闭文件
    text =f.read()
    f.close()


    if '混沌兽' in text:
        print(name)
