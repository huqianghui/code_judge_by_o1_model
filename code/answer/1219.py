color = ['灰色_', '紫色_', '绿色_', '黄色_', '蓝色_', '红色_']
shape = ['五边形', '半圆形', '梯形', '圆形', '三角形', '平行四边形']
for i in range(4):
    a = input()
    if a == 'red':
        r = color[5] + shape[4]
        print(r)
    elif a == 'green':
        r = color[2] + shape[0]
        print(r)
    else:
        r = color[1] + shape[5]
        print(r)