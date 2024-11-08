import pandas

data = pandas.read_csv('图灵大街.csv')

# 从data中取出'时间'大于9的数据
data1 = data[data['时间'] > 9]
# 从data中取出'时间'小于等于9的数据
data2 = data[data['时间'] <= 9]


print(data1)
print(data2)
