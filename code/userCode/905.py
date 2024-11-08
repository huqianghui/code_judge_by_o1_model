import requests

u = 'https://www.hetao101.com/api/color_telling'
d = open_deal_image('路口照片1.png')
a=requests.post(url=u,data=d)
print(a)
