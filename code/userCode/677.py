import pandas
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, recall_score

data = pandas.read_csv('心脏病数据.csv')
data['性别'] = data['性别'].replace(['男', '女'], [1, 2])
data['吸烟频率'] = data['吸烟频率'].replace(['从不', '极少', '偶尔', '经常'], [1, 2, 3, 4])
data['喝酒频率'] = data['喝酒频率'].replace(['从不', '极少', '偶尔', '经常'], [1, 2, 3, 4])
data['运动频率'] = data['运动频率'].replace(['从不', '极少', '偶尔', '经常'], [1, 2, 3, 4])
x_data = data.drop(columns=['有无患病风险'])
y_data = data['有无患病风险']
# x_train为 训练数据的特征
# y_train为 训练数据的结果
# x_test为  测试数据的特征
# y_test为  测试数据的结果
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3, random_state=1)
# ====训练并评估模型====
# 1、创建并训练模型
M = DecisionTreeClassifier(random_state = 1,max_depth =40)
M.fit(x_train,y_train)
# 2、使用模型对测试数据进行预测
N = M.predict(x_test)
# 3、用测试数据的真实结果和预测结果来评估模型


print('正确率:',accuracy_score(y_test,N))
print('召回率:',recall_score(y_test,N,average = None))




