import base64
import json
import requests
from PIL import Image


# 图片转字符串
def image_to_str(img_path):
    with open(img_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')
img_data = image_to_str('images/照片.png')


# 字符串转图片
def str_to_image(b64str):
    r_img_path = 'images/响应.png'
    data = base64.b64decode(b64str.encode('utf-8'))
    with open(r_img_path, 'wb') as f:
        f.write(data)
    return r_img_path


# 构造请求数据
url = 'http://htapi.hetao101.com/third-proxy-service/v1/uauth/body_seg'
headers = {'content-type': 'application/json'}
data = json.dumps({'image': img_data})

# 发送请求获取响应
r = requests.post(url=url, headers=headers, data=data)
if r.status_code == 200:
    print('请求成功')
    # 获取响应图片字符串
    r_img_data = r.json()['data']['foreground']

    # =====调用函数, 保存响应图片, 得到图片路径=====
    r_img_path = 

    print('图片保存成功')
    # 展示图片
    Image.open(r_img_path).show()




