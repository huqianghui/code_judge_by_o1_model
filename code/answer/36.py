import requests
import json

u = 'https://www.hetao101.com/api/classification'
img = open_deal_image('测试图片.png')
response = requests.post(url=u, data=img)
r = json.loads(response)
results = r['results']

s = 0
n = ''
# 遍历列表results, 找出可能性最大的分类
for j in results:
    if j['score'] > s:
        s = j['score']
        n = j['name']
       
print(n, s)
