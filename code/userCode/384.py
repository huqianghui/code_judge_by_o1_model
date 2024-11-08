import pandas
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = pandas.read_csv('电影数据.csv')

# 处理数据
data = data.drop(columns=['电影名称'])
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
train = data[:700]
test = data[700:]
x_train = train.drop(columns=['票房'])
y_train = train['票房']
x_test = test.drop(columns=['票房'])
y_test = test['票房']

# 训练线性回归模型
model = LinearRegression()
model.fit(x_train,y_train)

# 评估模型, 计算平均误差
p = model.predict(x_test)
mae = mean_absolute_error(y_test,p)

print('平均误差', mae)










