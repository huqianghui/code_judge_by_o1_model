import pandas

data = pandas.read_csv('空气等级数据.csv')

mean1 = data['湿度'].mean()
data['湿度'] = data['湿度'].fillna(mean1)

mean2 = data['气压'].mean()
data['气压'] = data['气压'].fillna(mean2)

mode = data['空气等级'].mode()[0]
data['空气等级'] = data['空气等级'].fillna(mode)

data['风向'] = data['风向'].replace(['东北风', '西北风', '东南风', '西南风'], [1, 2, 3, 4])
data['季节'] = data['季节'].replace(['春', '夏', '秋', '冬'], [1, 2, 3, 4])

# =======切片划分数据=======
# 共2200条数据, 取前1500条为训练数据, 后700条为测试数据
train = data[:1500]
x_train = train.drop(columns='空气等级')
y_train = train['空气等级']
test = data[1500:]
x_test = test.drop(columns='空气等级')
y_test = test['空气等级']
