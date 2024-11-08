import pandas

# 1.读取'通行证.csv'中的内容
f = pandas.read_csv('通行证.csv')

# 2.获取每一列数据
ci = f['磁力']
hou = f['厚度']
qing = f['清晰度']
result = f['真假']

# 3.分别计算三个特征与检测结果的相关性,并打印出来
ci_r = ci.corr(result)
print('磁力与检测结果的相关性:', ci_r)

hou_r = hou.corr(result)
print('厚度与检测结果的相关性:', hou_r)

qing_r = qing.corr(result)
print('清晰度与检测结果的相关性:', qing_r)
