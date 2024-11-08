import pandas
data = pandas.read_csv('调查数据.csv')
# 训练数据
train = data[:7000]
# 测试数据
test = data[7000:]
# 编写代码, 拆分"训练数据"的特征和结果
x_train = 
y_train = 
print('特征:', x_train)
print('结果:', y_train)