import pandas
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,recall_score
data = pandas.read_csv('调查数据.csv')
# 拆分训练和测试数据
train = data[:7000]
test = data[7000:]
# 拆分特征和结果
x_train = train.drop(columns=['购买意愿'])
y_train = train['购买意愿']
# 创建模型并训练
tree_model = DecisionTreeClassifier()
tree_model.fit(x_train, y_train)
# 评估模型
x_test = test.drop(columns=['购买意愿'])
y_test = test['购买意愿']
y_pre = tree_model.predict(x_test)
accuracy = accuracy_score(y_test, y_pre)
print('正确率:', accuracy)
recall_0 = recall_score(y_test, y_pre, pos_label=0)
print('0-召回率:', recall_0)
recall_1 = recall_score(y_test, y_pre, pos_label=1)
print('1-召回率:', recall_1)
# 使用模型对"预测数据.csv"文件中的数据进行预测
new_data = pandas.read_csv('预测数据.csv')
# 补全代码, 用: 模型.predict()对new_data数据进行预测
pre = 
new_data['购买意愿'] = pre
new_data.to_csv('结果.csv')
print('完成预测')







