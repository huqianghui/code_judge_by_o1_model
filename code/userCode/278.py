import pandas

data = pandas.read_csv('心脏病数据.csv')
# 把性别、吸烟频率、喝酒频率、运动频率 列数值化
data['性别'] = data['性别'].replace(['男', '女'], [1, 2])
data['吸烟频率'] = 
data['喝酒频率'] = 
data['运动频率'] = 
print(data)