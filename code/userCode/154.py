'''
书架上所有书籍的名字按顺序存储在列表books中.
books = [['格林童话', '飞机百科', ……],
         ['西游记', ……],
         ['百科全书1', ……]]
'''
# 编写代码, 打印出所有包含'故事'的书名, 并统计出这些书的总数
count=0
for n in books:
    for x in n:
        if '故事' in x:
            print(x)
            count+=1
print(count)