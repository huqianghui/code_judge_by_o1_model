from PIL import Image
import numpy as np
import os
###### 在这里编写代码 ######
# 导入神经网络模型
from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import  train_test_split



def get_data():
    data = {'features': [], 'labels': []}
    for img_name in os.listdir('images'):
        imgpath = 'images/' + img_name
        label = img_name[0]
        img = Image.open(imgpath).convert('L')
        img = img.resize((28, 28))
        img_num = np.array(img).reshape(-1)
        img_num = list(img_num)
        data['features'].append(img_num)
        data['labels'].append(int(label))

    return data


data = get_data()
x_train, x_test, y_train, y_test = train_test_split(data['features'], data['labels'], test_size=0.3, random_state=1)

###### 在这里编写代码 ######
# 创建神经网络模型
model =MLPClassifier()



print('模型创建成功')











