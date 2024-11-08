import pandas

data = pandas.read_csv('活动费用记录.csv')
num = data['人数']
money = data['费用']

# 调整参数a、b的值, 让误差低于40
a = 54
b = 94
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
print('误差:', s / len(predict))