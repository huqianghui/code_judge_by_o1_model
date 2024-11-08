import pandas

data = pandas.read_csv('活动费用记录.csv')
num = data['人数']
money = data['费用']

# 调整参数a的值, 让误差小于103
a = 62
predict = []
for x in num:
    y = a * x
    predict.append(y)

# 预测费用存储到了predict中
# 真实费用存储到了money中
# 补全代码, 计算出平均误差
s = 0
for i in range(len(predict)):
    if money[i] > predict[i]:
        s += money[i] - predict[i]
    else:
        s += predict[i] - money[i]
print('平均误差:', s / len(predict))
