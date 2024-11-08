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

# =====使用循环实现自动调参=====
while True:
# 计算各方向误差
    error = cal(a, b)
    print('误差:', error)
    a_down = cal(a - step, b)
    a_up = cal(a + step, b)
    b_down = cal(a, b - step)
    b_up = cal(a, b + step)

# 找到误差最小值
    min_error = min(error, a_down, a_up, b_down, b_up)

# =====如果当前误差是最小误差, 打印参数并停止循环=====
    if min_error == error:
        print('a:', a, 'b:', b)
        break
    
# 修改参数
    elif min_error == a_down:
        a -= step
    elif min_error == a_up:
        a += step
    elif min_error == b_down:
    b -= step
    elif min_error == b_up:
        b += step


