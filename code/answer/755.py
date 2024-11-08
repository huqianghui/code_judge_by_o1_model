import requests


def get_response(url):
    h = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=h)
    return response


def crawl_image(url):
    img_r = get_response(url)
    filename = url.split('/')[-1]
    f = open(filename, 'wb')
    f.write(img_r.content)
    f.close()


url = 'http://static.hetaoimg.com/emoji/images/高兴3.png'
crawl_image(url)