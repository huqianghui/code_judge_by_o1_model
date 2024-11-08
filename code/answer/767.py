import requests
from bs4 import BeautifulSoup


# 发送请求, 获取响应
def get_response(url):
    h = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

    response = requests.get(url, headers=h)
    response.encoding = response.apparent_encoding
    return response


# 爬取图片, 进行保存
def crawl_image(name, url):
    print(name + '.png 爬取中...')

    # 爬取图片
    img_r = get_response(url)
    img = img_r.content

    # 保存文件
    filename = 'images/' + name + '.png'
    f = open(filename, 'wb')
    f.write(img)
    f.close()

    print(name + '.png 已爬取')


# 爬取音乐, 进行保存
def crawl_music(name, url):
    print(name + '.mp3 爬取中...')

    # 爬取音乐
    music_r = get_response(url)
    music = music_r.content

    # 保存文件
    filename = 'music/' + name + '.mp3'
    f = open(filename, 'wb')
    f.write(music)
    f.close()

    print(name + '.mp3 已爬取')


# 向音乐网站发送请求, 获取响应
m_url = 'http://htapi.hetao101.com/pandora/music/list.html'
r = get_response(m_url)

if r.status_code == 200:
    # 解析页面
    soup = BeautifulSoup(r.text, 'html.parser')
    musics = soup.find_all('div', attrs={'class': 'music-item'})

    # 遍历音乐列表
    for i in musics:
        # 获取图片和mp3文件的链接以及歌曲名
        img_url = i.find('img')['src']
        music_url = i.find('audio')['src']
        name = i.find('span', attrs={'class': 'music-name'}).get_text()

        # 调用爬取图片的函数
        crawl_image(name, img_url)
        # 调用爬取歌曲的函数
        crawl_music(name, music_url)

    print('==爬取完毕==')
