import pandas

# 读取csv文件数据
data = pandas.read_csv('共享单车.csv')

# 去除相关性低于0.2的特征,并打印出来
d = data.drop(columns = [ '是否假期', '是否工作日', '日期' ] )
print(d)

