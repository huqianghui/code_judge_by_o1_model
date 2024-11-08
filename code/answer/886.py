from PIL import Image
import numpy
import os


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

# -----将特征数据转换为ndarray类型-----
features = numpy.array(features)
# -----使用reshape修改行列数-----
features = features.reshape(500, 7500)





