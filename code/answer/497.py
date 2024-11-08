from PIL import Image
import numpy as np
import os
from sklearn.neighbors import KNeighborsClassifier
import joblib


def get_data():
    data = {'x_train': [], 'y_train': []}
    for img_name in os.listdir('images'):
        imgpath = 'images/' + img_name
        label = img_name[0]
        img = Image.open(imgpath).convert('L')
        img = img.resize((28, 28))
        img_num = np.array(img).reshape(-1)
        img_num = list(img_num)
        data['x_train'].append(img_num)
        data['y_train'].append(int(label))

    return data

print('程序正在运行中...')
data = get_data()
x_train = data['x_train']
y_train = data['y_train']

model = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train, y_train)
joblib.dump(model, "手写数字.pkl")
print('模型已经保存好了')
