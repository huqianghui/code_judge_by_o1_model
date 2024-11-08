import requests
import json
import time
import pandas

#请求网页, 返回响应
def get_response_post(url, data):
    h = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    response = requests.post(url=url, headers=h, data=data)
    return response

url = 'http://htapi.hetao101.com/pandora-dev/v1/jp/virusCity/list'
data = json.dumps({'user':'hetao', 'passwd':'1024'})
url_city = 'http://htapi.hetao101.com/pandora-dev/v1/jp/virusCity/info'

virus_data = []

# 爬取首页
print('开始请求数据,请耐心等待...')
res = get_response_post(url, data)
if res.status_code == 200:
    r = json.loads(res.text)
    cities = r['cityInfo']['cityID']
    # 分别爬取每个城市的病毒数据
    for i in cities:
        data_city = json.dumps({'user':'hetao', 'passwd':'1024', 'id': i})
        res_city = get_response_post(url_city, data_city)
        if res_city.status_code == 200:
            r_city = json.loads(res_city.text)
            info = r_city['info']
            for k in info:
                if k['宿主'] == '人类':
                    virus_data.append(k)
        time.sleep(1)
        
# 将 中的数据存入''文件 
df =  pandas.DataFrame(virus_data)
df.to_csv('未知病毒.csv', index=False)


print('数据存储完成')