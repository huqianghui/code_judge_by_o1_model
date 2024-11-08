import requests

# 请求网页, 返回响应
def get_response(url):
    # 设置请求头参数, 伪装成浏览器访问
    h = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    # 发送请求, 获取响应
    response = requests.get(url = url,headers = h)
    # 返回响应数据
    return response

# 首页地址
url = 'http://htapi.hetao101.com/pandora/virus/home'

# 爬取首页,打印爬取到的html