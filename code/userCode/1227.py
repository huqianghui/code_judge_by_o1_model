shape =['蓝色_三角形', '黄色_圆形', '蓝色_圆形', '黄色_梯形', '绿色_圆形', '黄色_三角形']
for i in range(4):
    a = input()
    if a == 'green':
        r = shape[4]
        print(r)
    elif a == 'yellow':
        r = shape[3]
        print(r)
    else:
        r = shape[0]
        print(r)
