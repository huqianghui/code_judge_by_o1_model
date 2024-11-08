import base64


# 图片转字符串函数
def image_to_str(img_path):
    with open(img_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

# =====调用函数, 将images文件夹中'照片.png'转换为字符串=====
img_data = 

print(img_data[:100])
