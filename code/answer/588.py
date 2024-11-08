import pandas
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.model_selection import train_test_split

data = pandas.read_csv('空气等级数据.csv')

mean1 = data['湿度'].mean()
data['湿度'] = data['湿度'].fillna(mean1)

mean2 = data['气压'].mean()
data['气压'] = data['气压'].fillna(mean2)

data = data.dropna(subset=['空气等级'])

data['风向'] = data['风向'].replace(['东北风', '西北风', '东南风', '西南风'], [1, 2, 3, 4])
data['季节'] = data['季节'].replace(['春', '夏', '秋', '冬'], [1, 2, 3, 4])

# =======随机划分训练数据与测试数据=======
x = data.drop(columns = '空气等级')
y = data['空气等级']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

model = DecisionTreeClassifier()
model.fit(x_train, y_train)

y_pre = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pre)
recall = recall_score(y_test, y_pre, average=None)

print('正确率:', accuracy)
print('召回率:', recall)
