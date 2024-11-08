import requests
import json
def downloadData(username):
    url = 'http://htapi.hetao101.com/pandora-dev/v1/learning/data?username=' + username
    # 爬取数据并转换成字典格式返回




hemu = downloadData('禾木')
print(hemu)
