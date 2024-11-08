import requests
import time

# 请求网页, 返回响应
def get_response(url):
    # 设置请求头参数, 伪装成浏览器访问
    h = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    # 发送请求, 获取响应
    response = requests.get(url=url, headers=h)
    response.encoding = response.apparent_encoding
    # 返回响应数据
    return response


url = 'http://htapi.hetao101.com/pandora/idiom/s'
# 爬取所有页面, 并打印爬取到的html
for i in range(1, 21):
    print('======正在爬取第'+ str(i) + '页======')
    page_url = url+'?pn='+str(i)
    r = get_response(page_url)
    if r.status_code == 200:
        print(r.text)
    time.sleep(1)






