import requests
import time
import random
from bs4 import BeautifulSoup
import pandas

data = []
def parser_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    attr = {'class': 'info'}
    divs = soup.find_all('div', attrs=attr)
    for d in divs:
        name = d.find('h3')
        spans = d.find_all('span')
        movie_data = {}
        movie_data['电影名称'] = name.get_text()
        movie_data['导演'] = spans[0].get_text()
        movie_data['编剧'] = spans[1].get_text()
        movie_data['主演'] = spans[2].get_text()
        movie_data['类型'] = spans[3].get_text()
        movie_data['上映日期'] = spans[4].get_text()
        movie_data['时长'] = spans[5].get_text()
        movie_data['评分'] = spans[6].get_text()
        movie_data['评价人数'] = spans[7].get_text()
        movie_data['票房'] = spans[8].get_text().strip('万')
        data.append(movie_data)

root_url = 'http://htapi.hetao101.com/pandora/movie/'
h = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
for i in range(1, 6):
    
    movie_url = root_url + str(i) + '.html'
    filename = str(i) + '.html'
    r = requests.get(url=movie_url, headers=h)
    r.encoding = r.apparent_encoding
    info = r.text
    if r.status_code == 200:
        parser_html(info)
    print('数据下载、解析中...已完成:' + str(i*20) + '%')
    time.sleep(1)


# 将列表data中的数据转换成DataFrame格式
df = pandas.DataFrame(data)
# 将转化后的数据df存入名为: '电影数据.csv' 的文件中
df.to_csv('电影数据.csv', index=False)

print('数据存储完成')















