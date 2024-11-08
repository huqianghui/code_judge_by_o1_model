import pandas

f = pandas.read_csv('魔力手环.csv')

hard = f['硬度']
size = f['大小']
color = f['颜色']
result = f['是否合格']

# 计算每个特征和结果的相关性
hard_r = hard.corr(result)
size_r = size.corr(result)
color_r = color.corr(result)

print('硬度与结果的相关性:',   )
print('大小与结果的相关性:',   )
print('颜色与结果的相关性:',   )







