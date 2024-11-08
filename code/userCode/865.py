import requests, base64, json

# 图片转base64字符串
def image_to_str(img_path):
    with open(img_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

# 服务接口
url = 'http://htapi.hetao101.com/third-proxy-service/v1/uauth/handwriting'
# 构造请求头
headers = {'content-type': 'application/json'}
# 构造请求体
img_data = image_to_str('images/作文1.png')
data = json.dumps({'image': img_data})
# 调用接口, 发送请求
r = requests.post(url=url, headers=headers, data=data)
if r.status_code == 200:
    s = r.json()
    if s['errcode'] == 0:
        # ====分析响应信息, 解析出文字并打印出来====
        words_result=s['data']['words_result']
        words=''
        for w in words_result:
            words += w['words']
        print(words)
else:
    print('请求, 错误码:', r.status_code)








