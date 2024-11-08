import requests

def get_response(url):
    h = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    # =======在下方编写代码=====
    # 发送请求, 获取响应
    response = requests.get(url,headers=h)
    # 返回响应数据
    return response

url = 'http://static.hetaoimg.com/emoji/images/高兴3.png'
r = get_response(url)