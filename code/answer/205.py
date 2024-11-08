from matplotlib import pyplot

pyplot.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei']

names = ['赤洋', '金翼漠', '海岛', '中央岛', '酸浆林']
area = [8900, 16700, 21700, 35400, 53300]

# 使用barh()函数绘制水平柱状图
pyplot.barh(names, area)
# 给图表添加x轴标签、y轴标签
pyplot.xlabel('面积')
pyplot.ylabel('基地名称')

print('水平柱状图绘制中...')
pyplot.show()