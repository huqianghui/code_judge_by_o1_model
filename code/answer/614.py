from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy
import os
import joblib


# 处理图片函数
def process_img(img_path):
    img = Image.open(img_path).convert('RGB')  # 打开图片并转换为RGB模式
    img = img.resize((50, 50))  # 重设图片尺寸
    img_num = numpy.array(img)  # 图片转换为数值数据
    return img_num  # 返回数值数据


features = []  # 存储特征的列表
labels = []  # 存储结果的列表

# 构造特征数据和结果数据
for img_name in os.listdir('emojis'):
    img_path = 'emojis/' + img_name  # 拼接图片路径
    img_num = process_img(img_path)  # 将图片转换为数值数据
    features.append(img_num)  # 存储特征

    img_label = img_name[:2]  # 切片获取图片类别
    labels.append(img_label)  # 存储结果

features = numpy.array(features)  # 转换类型
features = features.reshape(500, 7500)  # 修改行列数

# 随机划分数据
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=1)

# -----更换为随机森林模型并调参优化-----
model = RandomForestClassifier(n_estimators=220)

model.fit(X_train, y_train)  # 训练
y_pred = model.predict(X_test)  # 预测
print('正确率:', accuracy_score(y_test, y_pred))  # 评估

# -----保存模型-----
joblib.dump(model, '表情识别.pkl')




