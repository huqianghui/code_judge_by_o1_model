import base64
import json
import requests


# 图片转字符串
def image_to_str(img_path):
    with open(img_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')
img_data = image_to_str('images/照片.png')


# 构造请求数据
url = 'http://htapi.hetao101.com/third-proxy-service/v1/uauth/body_seg'
# 请求头
headers = {'content-type': 'application/json'}

# =====构造请求体=====
data = json.dumps({'image':img_data})

# =====发送请求获取响应=====
r = requests.post(url=url, headers=headers, data=data)

if r.status_code == 200:
    print('请求成功')
