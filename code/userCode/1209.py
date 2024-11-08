import pandas
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,recall_score

data = pandas.read_csv('企鹅数据.csv')

# 处理数据
data['喙的长度'] = data['喙的长度'].fillna(44.96)
data['喙的厚度'] = data['喙的厚度'].fillna(17.24)
data['鳍的长度'] = data['鳍的长度'].fillna(200.89)
data['体重'] = data['体重'].fillna(4162.81)
data['性别'] = data['性别'].fillna('Female')
data['性别'] = data['性别'].replace(['Male', 'Female'], [1, 2])

# 训练模型
train = data[:700]
x_train = train.drop(columns=['企鹅'])
y_train = train['企鹅']
model = DecisionTreeClassifier()
model.fit(x_train, y_train)

# 拆分测试数据的特征与结果
test = data[700:]
x_test = 
y_test = 

# 用训练好的模型进行预测
y_pre = 

# 评估模型, 计算正确率和召回率
accuracy = 
recall = 

print('正确率:', accuracy)
print('召回率:', recall)
