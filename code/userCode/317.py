import pandas

data = pandas.read_csv('企鹅数据.csv')

# 填充每个特征列中的缺失数据
data['喙的长度'] = 
data['喙的厚度'] = 
data['鳍的长度'] = 
data['体重'] = 
data['性别'] = 

print(data.isna().sum())