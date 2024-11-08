import pandas

# 读取csv文件数据
data = pandas.read_csv('共享单车.csv')

# 去除相关性低于0.2的特征
data1 = data.drop(columns=['是否假期', '是否工作日', '日期'])

# 将数据拆分成测试数据和训练数据


print('用于训练模型的数据:',[:7000])
print('用于评估模型的数据:',[7000:])
