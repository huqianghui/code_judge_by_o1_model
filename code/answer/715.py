import requests

# 要爬取的网址
url = 'http://htapi.hetao101.com/pandora/sp1/sight.html'

# 发送请求获取响应
r = requests.get(url=url)

# =======打印状态码=======
print('状态码:', r.status_code)