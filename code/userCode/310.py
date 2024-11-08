import requests
from bs4 import BeautifulSoup


# 发送请求, 获取响应
def get_response(url):
    h = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

    response = requests.get(url, headers=h)
    response.encoding = response.apparent_encoding
    return response


# 向音乐网站发送请求, 获取响应
m_url = 'http://htapi.hetao101.com/pandora/music/list.html'
r = get_response(m_url)

if r.status_code == 200:
    # 解析页面
    soup = BeautifulSoup(r.text, 'html.parser')
    musics = soup.find_all('div', attrs={'class': 'music-item'})

    # 遍历音乐列表
    for i in musics:
        # 获取图片链接
        img_url =

        # 获取mp3链接
        music_url =

        # 获取歌曲名
        name =

        print('歌曲名:', name)
        print('图片链接:', img_url)
        print('mp3链接:', music_url)