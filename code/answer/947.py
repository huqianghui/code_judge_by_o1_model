color = ['黄色_', '绿色_', '蓝色_', '红色_']
shape = ['五边形', '三角形', '圆形', '梯形']
for i in range(3):
    a = input()
    if a == 'yellow':
        r = color[0] + shape[2]
        print(r)
    else:
        r = color[3] + shape[1]
        print(r)