import pandas

# 读取人流量数据
a=pandas.read_csv('记录.csv')
people=a['人流量']

# 遍历人流量数据, 计算对应的销售额
pre_sale =[]
for x in people:
    b=people[x]*12
    b+=pre_sale

print(pre_sale)