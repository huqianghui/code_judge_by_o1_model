import pandas

data = pandas.read_csv('企鹅数据.csv')

# 填充每个特征列中的缺失数据
data['喙的长度'] = data['喙的长度'].fillna(44.96)
data['喙的厚度'] = data['喙的厚度'].fillna(17.24)
data['鳍的长度'] = data['鳍的长度'].fillna(200.89)
data['体重'] = data['体重'].fillna(4162.81)
data['性别'] = data['性别'].fillna('Female')

print(data.isna().sum())
