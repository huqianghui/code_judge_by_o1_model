info = [['山', '颜', '水', '色'],
        ['五', '彩', '十', '色'],
        ['湖', '面', '山', '色'],
        ['一', '扫', '而', '光']]
c = ['乐', '好', '地', '光']



for i in info:
    if i[3]=='色':
        i[1]=c[3]
print(info)