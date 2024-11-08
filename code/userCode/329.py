import requests

def get_response(url):
    h = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=h)
    return response
    
# =====在函数中编写代码=====  
def crawl_image(url):
    # 调用get_response函数对图片链接发起请求
    img_r=get_response(url)
    # 设置文件名
    filename = '高兴3.png'
    # 以'wb'方式打开文件
    f=open(filename,'wb')
    # 将响应数据的content属性值写入文件
    f.write(img_r.content)
    # 关闭文件
    f.close()


url = 'http://static.hetaoimg.com/emoji/images/高兴3.png'
crawl_image(url)








