import pandas

data = pandas.read_csv('电影数据.csv')
data = data.drop(columns=['电影名称'])

# 数据数值化
info1 = pandas.read_csv('电影类型喜爱度.csv')
category = list(info1['类型'])
poll = list(info1['喜爱度'])
data['类型'] = data['类型'].replace(category, poll)
info2 = pandas.read_csv('人物喜爱度.csv')
name = list(info2['姓名'])
like = list(info2['喜爱度'])
data = data.replace(name, like)
date = []
for i in data['上映日期']:
    i = i.split('/')
    i[1] = i[1].zfill(2)
    i[2] = i[2].zfill(2)
    i = ''.join(i)
    date.append(int(i))
data['上映日期'] = pandas.DataFrame(date)

# 参考左侧提示, 将数据划分为训练数据和测试数据
train = data[:700]
test = data[700:]

# 分别取出训练数据中的特征列和结果列
x_train = train.drop(columns=['票房'])
y_train = train['票房']
# 分别取出测试数据中的特征列和结果列
x_test = test.drop(columns=['票房'])
y_test = test['票房']

print('拆分完成')






