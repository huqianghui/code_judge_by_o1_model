hetao = {'2252': '对', '2384': '肤', '2420': '复', '2828': '技', '2865': '坚', '3141': '可', '3660': '能', '3804': '皮', '3888': '气', '4181': '神', '4254': '手', '5052': '以', '5118': '硬', '5141': '由', '5438': '制', '5552': '自'}
f1 = open('文件5.txt', 'r', encoding='utf-8')
lines = f1.readlines()
f1.close()
info = lines[2:]
length = len(info)
for i in range(length):
    info[i] = info[i].strip('\n')
word = ''
for i in info:
    w = hetao[i]
    word += w

# 将解密信息word写入文件 混沌兽.txt
# 1.打开'混沌兽.txt'文件
f2 = open('混沌兽.txt', 'w', encoding='utf-8')
# 2.将解密信息word写入文件
f2.write(word)
# 3.关闭文件
f2.close()