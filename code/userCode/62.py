import pandas

data = pandas.read_csv('记录.csv')
# 编写代码, 把数据按照温度大小排序
data = data.sort_values('温度')
