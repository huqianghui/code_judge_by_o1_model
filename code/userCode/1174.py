import pandas

data = pandas.read_csv('能耗数据.csv')
# 特征: 机器数量number
number = data['机器数量']
# 真实能耗energy
energy = data['能耗']


# ====定义计算误差函数cal()=====
# 传入关系式的两个参数a、b, 返回该参数下的平均误差
def cal(a, b):
    s = 0
    for i in range(len(number)):
        predict = a * number[i] + b
        if energy[i] > predict:
            s += energy[i] - predict
        else:
            s += predict - energy[i]
# =====函数返回平均误差=====
return s / len(number)
# 参数初始值
a = 90
b = 0
# 步长
step = 5

# 计算当前误差
error = cal(a, b)
print('当前误差:', error)

# =====计算a减小后误差=====
a_down = cal(a-step, b)
print('a减小后误差:', a_down)

# =====计算a增加后误差=====
a_up = cal(a+step, b)
print('a增加后误差:', a_up)

# =====计算b减小后误差=====
b_down = cal(a, b-step)
print('b减小后误差:', b_down)

# =====计算b增加后误差=====
b_up = cal(a, b+step)
print('b增加后误差:', b_up)


