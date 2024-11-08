import pandas
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score

data = pandas.read_csv('空气等级数据.csv')

mean1 = data['湿度'].mean()
data['湿度'] = data['湿度'].fillna(mean1)

mean2 = data['气压'].mean()
data['气压'] = data['气压'].fillna(mean2)

# =======删除结果列中缺失值所在的行=======
data = data.dropna(subset=['空气等级'])


data['风向'] = data['风向'].replace(['东北风', '西北风', '东南风', '西南风'], [1, 2, 3, 4])
data['季节'] = data['季节'].replace(['春', '夏', '秋', '冬'], [1, 2, 3, 4])

train = data[:1500]
x_train = train.drop(columns='空气等级')
y_train = train['空气等级']
test = data[1500:]
x_test = test.drop(columns='空气等级')
y_test = test['空气等级']

model = DecisionTreeClassifier()
model.fit(x_train, y_train)

y_pre = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pre)
recall = recall_score(y_test, y_pre, average=None)

print('正确率:', accuracy)
print('召回率:', recall)
