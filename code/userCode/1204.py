hetao = {'2252': '对', '2384': '肤', '2420': '复', '2828': '技', '2865': '坚', '3141': '可', '3660': '能', '3804': '皮', '3888': '气', '4181': '神', '4254': '手', '5052': '以', '5118': '硬', '5141': '由', '5438': '制', '5552': '自'}
f1 = open('文件5.txt', 'r', encoding='utf-8')
lines = f1.readlines()
f1.close()
info = lines[2:]
length = len(info)
for i in range(length):
    info[i] = info[i].strip('\n')

# 遍历列表info得到数字编码, 并把数字编码对应的汉字打印出来
for i in info:
    print(hetao[i])

