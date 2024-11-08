import requests
import time
import random

root_url = 'http://htapi.hetao101.com/pandora/movie/'
h = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

for i in range(1, 51):
    movie_url = root_url + str(i) + '.html'
    filename = str(i) + '.html'

    # 发送请求获取响应
    r = requests.get(url = movie_url, headers=h)
    r.encoding = r.apparent_encoding
    info = r.text

    # 保存爬取下来的网页
    f = open(filename, 'w', encoding='utf-8')
    f.write(info)
    f.close()
    print(filename + '保存成功')

    # 让程序暂停几秒, 避免请求发送过于频繁
    time.sleep(1)