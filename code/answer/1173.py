import requests
import json
def downloadData(username):
    url = 'http://htapi.hetao101.com/pandora-dev/v1/learning/data?username=' + username
    data = requests.get(url)
    data = json.loads(data.text)
    return data
hemu = downloadData('禾木')
print(hemu)
