import json
s = input()
# json转字典
r = json.loads(s)
# 获取国家名称
country = r['country']
print('国家名称:', country)
# 获取排名
rank = r['rank']
print('排名:', rank)