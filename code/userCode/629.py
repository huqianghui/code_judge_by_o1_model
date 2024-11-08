'''
书架上所有书籍的名字按顺序存储在列表books中.
books = [['格林童话', ……],
         ['西游记', ……],
         ……
         ['哈利波特1', ……]]
'''
# 百科全书 分为1, 2两册
# 找到每本 百科全书 在书架上的具体位置
for i in range(4):
    for j in range(len(books[i])):
        if books[i][j] == '百科全书1' or books[i][j] == '百科全书2':
            print(i+1,j+1)