'''
书架上所有书籍的名字按顺序存储在列表books中.
books = [['格林童话', '飞机百科', ……],
         ['西游记', ……],
         ['百科全书1', ……]]
'''
for x in books:
    for b in x:
        if b == '西游记':
            print('yes')
        else:
            print('no')