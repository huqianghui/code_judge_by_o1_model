'''
书架上所有书籍的名字按顺序存储在列表books中.
books = [['格林童话', '飞机百科', ……],
         ['西游记', ……],
         ['百科全书1', ……]]
'''
# 统计出'百科全书'共有多少本
count = 0
for x in books:
    for b in x:
        if b=='百科全书1' or '百科全书2':
            count += 1
print(count)
