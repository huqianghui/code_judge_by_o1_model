import pandas
data = pandas.read_csv('调查数据.csv')
# 训练数据
train = data[:7000]
# 测试数据
test = data[7000:]

x_train = train.drop(columns=['购买意愿'])
y_train = train['购买意愿']
print('特征:', x_train)
print('结果:', y_train)


