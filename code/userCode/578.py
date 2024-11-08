import pandas
import pgzrun

df = pandas.read_csv('野牛数据.csv')
body = df['身长']
food = df['日均食量']
weight = df['体重']


# 函数功能: 传入3个参数的值, 返回对应的误差
def cal(a, b, c):
    predict = []
    for i in range(len(weight)):
        x1 = body[i]
        x2 = food[i]
        y = a * x1 + b * x2 + c
        predict.append(y)
    # 编写代码, 计算平均误差
    s = 0
    for i in range(len(weight)):
        if predict[i] > weight[i]:
            s += predict[i] - weight[i]
        else:
            s += weight[i] - predict[i]
    return round(s / len(weight), 1)


# 参数初始值
a = 0.3
b = 11
c = 10
# 步长值
step_a = 0.1
step_b = 2
step_c = 1
WIDTH = 800
HEIGHT = 600
# 参数加号按钮
a_plus = Actor('加号按钮.png', (47, 41))
b_plus = Actor('加号按钮.png', (327, 41))
c_plus = Actor('加号按钮.png', (607, 41))
# 参数减号按钮
a_sub = Actor('减号按钮.png', (195, 41))
b_sub = Actor('减号按钮.png', (475, 41))
c_sub = Actor('减号按钮.png', (755, 41))
# 步长加号按钮
step_a_plus = Actor('加号按钮02.png', (47, 110))
step_b_plus = Actor('加号按钮02.png', (327, 110))
step_c_plus = Actor('加号按钮02.png', (607, 110))
# 步长减号按钮
step_a_sub = Actor('减号按钮02.png', (195, 110))
step_b_sub = Actor('减号按钮02.png', (475, 110))
step_c_sub = Actor('减号按钮02.png', (755, 110))
# 6个方向的误差对应矩形的坐标
a_plus_rect = (158, 530)
a_sub_rect = (272, 530)
b_plus_rect = (382, 530)
b_sub_rect = (488, 530)
c_plus_rect = (593, 530)
c_sub_rect = (698, 530)


def draw():
    screen.blit('背景', (0, 0))
    # 绘制参数, 步长, 加号, 减号
    screen.draw.text(str(a), (100, 30), color='black', fontsize=40)
    a_plus.draw()
    a_sub.draw()

    screen.draw.text(str(b), (385, 30), color='black', fontsize=40)
    b_plus.draw()
    b_sub.draw()

    screen.draw.text(str(c), (665, 30), color='black', fontsize=40)
    c_plus.draw()
    c_sub.draw()

    screen.draw.text(str(step_a), (100, 100), color='black', fontsize=40)
    step_a_plus.draw()
    step_a_sub.draw()

    screen.draw.text(str(step_b), (385, 100), color='black', fontsize=40)
    step_b_plus.draw()
    step_b_sub.draw()

    screen.draw.text(str(step_c), (665, 100), color='black', fontsize=40)
    step_c_plus.draw()
    step_c_sub.draw()

    # 绘制代表当前误差的矩形
    draw_rect((50, 530), 50, cal(a, b, c))
    # ==========请在下方编写代码==========
    # 编写代码, 计算6个方向的误差, 并绘制对应的矩形
    # a增加step_a的方向
    draw_rect(a_plus_rect, 50, cal(a + step_a, b, c))
    # a减少step_a的方向
    draw_rect(a_sub_rect, 50, cal(a - step_a, b, c))
    # b增加step_b的方向
    draw_rect(b_plus_rect, 50, cal(a, b + step_b, c))
    # b减少step_b的方向
    draw_rect(b_sub_rect, 50, cal(a, b - step_b, c))
    # c增加step_c的方向
    draw_rect(c_plus_rect, 50,cal(a, b, c+step_c))
    # c减少step_c的方向
    draw_rect(c_sub_rect, 50,cal(a, b, c-step_c))
    # ==========代码编写到此结束=========



pgzrun.go()
