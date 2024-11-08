import requests
import json
import os
# 导入shutil库
import shutil

img_list = os.listdir('相册')

for img in img_list:
    d = open_deal_image('相册/' + img)
    u = 'https://www.hetao101.com/api/cat'
    r = requests.post(url=u, data=d)
    r = json.loads(r)

    if r['results'][0]['score'] > 0.5:
        print(img, '猫')
        # 将"相册"中有猫的图片移动到"cats"文件夹
        shutil.move('相册/' + img, 'cats')
    else:
        print(img, '其他')
