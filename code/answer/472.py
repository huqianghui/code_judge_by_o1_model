from PIL import Image
import numpy


# 处理图片函数
def process_img(img_path):
    # 打开图片, 转换为RGB模式
    img = Image.open(img_path).convert('RGB')
    # -----将图片尺寸设置为50*50-----
    img = img.resize((50, 50))
    # -----将图片转换为数值数据-----
    img_num = numpy.array(img)
    # -----返回数值数据------
    return img_num


img_num = process_img('emojis/愤怒1.png')
print(img_num)

