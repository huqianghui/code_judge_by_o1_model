import requests
from bs4 import BeautifulSoup


def get_response(url):
    h = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=h)
    return response


def parser_info(html):
    urllist = []
    soup = BeautifulSoup(html, 'html.parser')
    alist = soup.find_all('a')
    for a in alist:
        url = a['href']
        urllist.append(url)
    return urllist


def parser_imageUrl(html):
    imgurllist = []
    soup = BeautifulSoup(html, 'html.parser')
    attr = {'class': 'image'}
    imglist = soup.find_all('img', attrs=attr)
    for img in imglist:
        imgurl = img['src']
        imgurllist.append(imgurl)
    return imgurllist


def crawl_image(url):
    img_r = get_response(url)
    filename = url.split('/')[-1]
    f = open(filename, 'wb')
    f.write(img_r.content)
    f.close()
    print(filename + '爬取成功!')

# 首页链接
url = 'http://htapi.hetao101.com/pandora/emoji/emojiKind.html'

# 调用get_response()函数获得首页的响应数据
r1 = get_response(url)
if r1.status_code == 200:
    # 调用parser_info()函数解析出子页面链接
    urllist = parser_info(r1.text)
    # 遍历子页面链接
    for u in urllist:
        # =====请在下方编写代码=====
        # 调用get_response()函数获得响应数据
        r2 = get_response(u)
        if r2.status_code == 200:
            # 调用parser_imageUrl()函数解析出子页面的图片链接
            imgurllist = parser_imageUrl(r2.text)
            # 遍历子页面图片链接
            for imgurl in imgurllist:
                # 调用crawl_image()函数爬取图片
                crawl_image(imgurl)











































