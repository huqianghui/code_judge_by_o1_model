import requests

movie_url = 'http://htapi.hetao101.com/pandora/movie/1.html'

# 发送请求,获得响应
r = requests.get(url=movie_url)


# 打印响应内容
info =r.text
print('响应内容字符串:', info)

# 保存html文件
filename = '1.html'
f = open(filename, 'w', encoding='utf-8')
f.write(info)
f.close()
print('保存成功')