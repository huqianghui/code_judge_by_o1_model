import requests
import json
import time

#请求网页, 返回响应
def get_response_post(url, data):
    h = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    response = requests.post(url=url, headers=h, data=data)
    return response

# 设置首页数据接口地址
url = 'http://htapi.hetao101.com/pandora-dev/v1/jp/virusCity/list'
# 设置首页的请求体
data = json.dumps({'user':'hetao', 'passwd':'1024'})
# 设置子页数据接口地址
url_city = 'http://htapi.hetao101.com/pandora-dev/v1/jp/virusCity/info'

# 爬取首页
res = get_response_post(url, data)
if res.status_code == 200:
    r = json.loads(res.text)
    # 列表cities中存储着所有城市ID
    cities = r['cityInfo']['cityID']
    # 分别爬取每个城市的病毒数据
    for i in cities:
        # 设置每个城市子页的请求体
        data_city = json.dumps({'user':'hetao', 'passwd':'1024', 'id': i})
        # 请求每个城市子页的数据
        res_city = get_response_post(url_city, data_city)
        # 解析返回的json数据
        if res_city.status_code == 200:
            r_city = json.loads(res_city.text)
            print(r_city)
        time.sleep(1)