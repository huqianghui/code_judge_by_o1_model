import pandas

data = pandas.read_csv('射击记录.csv')
# 将数据排序并存储在sorted_data中
sorted_data=data.sort_values('目标距离')

print(sorted_data)
