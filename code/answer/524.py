shape = ['黄色_三角形', '黄色_圆形',  '蓝色_圆形', '蓝色_三角形']
for i in range(3):
    a = input()
    if a == 'yellow':
        r = shape[0]
        print(r)
    else:
        r = shape[2]  
        print(r)