import pandas

data = pandas.read_csv('企鹅数据.csv')

# 计算每个特征列的填充数值并打印出来
print('喙的长度',data['喙的长度'].mean())
print('喙的厚度',data['喙的厚度'].mean())
print('鳍的长度', data['鳍的长度'].mean())
print('体重',data['体重'].mean())
print('性别', data['性别'].mode () )
