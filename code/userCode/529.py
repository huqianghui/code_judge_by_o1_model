import pandas

data = pandas.read_csv('足迹实验.csv')
shoe = data['鞋印长度']
step = data['步长']
height = data['身高']

a = 5
b = 3
c = 5

predict = []
# 对每一条数据进行预测,将预测出的身高存储在列表 predict 中
for i in range(len(shoe)):
    x1 = shoe[i]
    x2 = step[i]
    s = a * x1 + b * x2 + c
    predict.append(s)

print(predict)
