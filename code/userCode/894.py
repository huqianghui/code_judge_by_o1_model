import requests
from bs4 import BeautifulSoup 
 
url = 'http://htapi.hetao101.com/pandora/sp3/code.html'
h = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
r = requests.get(url=url, headers=h)
if r.status_code == 200:
    soup = BeautifulSoup(r.text, 'html.parser')
    # 解析出所有科目的名字、简介、学习时间
    # 取出所有div标签
    divs = soup.find_all('div')
    for div in divs:
        # 取出每一个div中的h2标签和p标签
        h2 = div.find_alll('h2')
        p = div.find_all('p')
        print('名字:',h2.get_text())
        print('简介:',p[0].get_text())
        print('学习时间:',     )




