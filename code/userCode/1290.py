import pandas

data = pandas.read_csv('能耗数据.csv')
# 特征: 机器数量number
number = data['机器数量']
# 真实能耗energy
energy = data['能耗']


# 计算误差函数cal
def cal(a, b):
    s = 0
    for i in range(len(number)):
        predict = a * number[i] + b
        if energy[i] > predict:
            s += energy[i] - predict
        else:
            s += predict - energy[i]
    return s / len(number)


# 参数初始值
a = 90
b = 0
# 步长
step = 5

# 计算各方向误差
error = cal(a, b)
print('当前误差:', error)
a_down = cal(a - step, b)
print('a减小后误差:', a_down)
a_up = cal(a + step, b)
print('a增加后误差:', a_up)
b_down = cal(a, b - step)
print('b减小后误差:', b_down)
b_up = cal(a, b + step)
print('b增加后误差:', b_up)


# ==========找到最小误差==========
min_error = min(                )

# =====找到最小误差对应的方向=====
if                    :
    print('参数不变')
elif                  :
    print('a减小')
elif                  :
    print('a增加')
elif                  :
    print('b减小')
elif                  :
    print('b增加')


