import pandas

data = pandas.read_csv('心脏病数据.csv')

data['性别'] = data['性别'].replace(['男', '女'], [1, 2])
data['吸烟频率'] = data['吸烟频率'].replace(['从不', '极少', '偶尔', '经常'], [1, 2, 3, 4])
data['喝酒频率'] = data['喝酒频率'].replace(['从不', '极少', '偶尔', '经常'], [1, 2, 3, 4])
data['运动频率'] = data['运动频率'].replace(['从不', '极少', '偶尔', '经常'], [1, 2, 3, 4])

print(data)
