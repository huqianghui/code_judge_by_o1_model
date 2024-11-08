import pandas
from sklearn.tree import DecisionTreeClassifier
data = pandas.read_csv('调查数据.csv')
# 拆分训练、测试数据
train = data[:7000]
test = data[7000:]
# 得到训练数据的特征
x_train = train.drop(columns=['购买意愿'])
# 得到训练数据的结果
y_train = train['购买意愿']
# 编写代码, 创建决策树模型并训练
tree_a=DecisionTreeClassifier()
tree_a.fit(x_train,y_train)
print('训练完成')