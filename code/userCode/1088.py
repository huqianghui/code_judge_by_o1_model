import pandas

data = pandas.read_csv('活动费用记录.csv')
num = data['人数']
money = data['费用']

# 函数功能: 传入两个参数, 返回这两个参数对应的误差
def cal(a, b):
    predict = []
    for x in num:
        y = a * x + b
        predict.append(y)
    
    s = 0
    for i in range(len(predict)):
        if money[i] > predict[i]:
            s += money[i] - predict[i]
        else:
            s += predict[i] - money[i]
    # round()函数功能: 保留两位小数
    return round(s / len(predict), 2)

a = 57
b = 140
n = cal(a, b)
print('当前误差:', n)

# 编写代码, 计算四个方向的误差
n = cal(a,b-1)
print('a b-1误差:', n)
n = cal(a,b+1)
print('a b+1误差:', n)
n = cal(a-1,b)
print('a-1 b误差:', n)
n = cal(a+1,b)
print('a+1 b误差:', n)












