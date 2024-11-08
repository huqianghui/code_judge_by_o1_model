import requests
from bs4 import BeautifulSoup
 
url = 'http://htapi.hetao101.com/pandora/sp3/xueqiu.html'
h = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
r = requests.get(url=url, headers=h)
if r.status_code == 200:
    # 解析出雪球的技能,注意:要先创建解析器再进行解析
    soup = BeautifulSoup(r.text, 'html.parser')    
    div = soup.find('div')
    p = div.find('p')
    print('技能:', p.get_text())