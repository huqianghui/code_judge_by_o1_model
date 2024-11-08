import requests
from bs4 import BeautifulSoup

def get_response(url):
    h = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=h)
    return response
 
# 解析主页, 得到子页面的链接
def parser_info(html):
    # =====在下方编写代码=====
    # 构造解析器
    soup = BeautifulSoup(html,'html.parser')
    # 解析出所有的a标签
    alist = soup.find_all('a')
    return alist


url = 'http://htapi.hetao101.com/pandora/emoji/emojiKind.html'
r = get_response(url)
if r.status_code == 200:
    alist = parser_info(r.text)
    print(alist)









    
