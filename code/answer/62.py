import pandas
data = pandas.read_csv('记录.csv')

data = data.sort_values('温度')
print(data)
