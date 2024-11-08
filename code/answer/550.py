import pandas
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# 数据处理
data = pandas.read_csv('共享单车.csv')
data1 = data.drop(columns=['是否假期','是否工作日','日期'])
train = data1[:7000]
test = data1[7000:]

# 创建&训练模型
y_train = train['租赁数量']
x_train = train.drop(columns=['租赁数量'])
lr_model = LinearRegression()
lr_model.fit(x_train, y_train)

# 评估模型
# 从测试数据中，得到特征列和结果列
x_test = test.drop(columns=['租赁数量'])
y_test = test['租赁数量']
# 计算预测值
y_test_pre = lr_model.predict(x_test)
# 计算平均误差
mae = mean_absolute_error(y_test, y_test_pre)

print('平均误差', mae)