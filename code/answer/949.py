import pandas

data = pandas.read_csv('调查数据.csv')
train = data[:7000]
test = data[7000:]
print('训练数据:', train)
print('测试数据:', test)



