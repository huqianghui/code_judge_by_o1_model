import pandas
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, recall_score

data = pandas.read_csv('心脏病数据.csv')

data['性别'] = data['性别'].replace(['男', '女'], [1, 2])
data['吸烟频率'] = data['吸烟频率'].replace(['从不', '极少', '偶尔', '经常'], [1, 2, 3, 4])
data['喝酒频率'] = data['喝酒频率'].replace(['从不', '极少', '偶尔', '经常'], [1, 2, 3, 4])
data['运动频率'] = data['运动频率'].replace(['从不', '极少', '偶尔', '经常'], [1, 2, 3, 4])

x_data = data.drop(columns=['有无患病风险'])
y_data = data['有无患病风险']
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3, random_state=1)

# 修改代码, 创建k近邻模型, 并优化模型
model = KNeighborsClassifier(n_neighbors=8)
model.fit(x_train, y_train)
y = model.predict(x_test)
accuracy = accuracy_score(y_test, y)
recall = recall_score(y_test, y, average=None)

print('正确率:', accuracy)
print('召回率:', recall)














