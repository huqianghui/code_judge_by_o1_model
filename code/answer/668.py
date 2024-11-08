import requests

root_url = 'http://htapi.hetao101.com/pandora/movie/'

# 拼接每一页的网址,并打印出来
for i in range(1, 51):
    movie_url = root_url + str(i) + '.html'
    print(movie_url)