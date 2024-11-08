import pandas

data = pandas.read_csv('记录.csv')
people = data['人流量']

pre_sale = []
real_sale = data['销售额']

for x in people:
    # 调整参数,减小误差
    y =  * x
    pre_sale.append(y)



num = len(pre_sale)
s = 0
for i in range(num):
    if pre_sale[i] >= real_sale[i]:
        s += pre_sale[i] - real_sale[i]
    else:
        s += real_sale[i] - pre_sale[i]

print('平均误差:', s / num)
