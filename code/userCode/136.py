import requests
import time
from bs4 import BeautifulSoup

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
    page_url = url + '?pn=' + str(i)
    r = get_response(page_url)
    if r.status_code == 200:
        # 构造解析器
        soup = BeautifulSoup(r.text, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'idiom'})
        # 解析出成语及图片的url
        for div in divs:
            name = div.find("b")
            pic = div.find("img")
            print('成语:',    name.get_text()   )
            print('图片url:',  pic.get()  )       
    time.sleep(1)





