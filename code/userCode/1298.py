from matplotlib import pyplot

pyplot.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'simhei']

names = ['禾木', '桃子', '乌拉乎', '麦杰', '麦琪']
points = [35, 35, 23, 32, 27]

pyplot.bar(names, points)
pyplot.title('战斗力统计图')
pyplot.xlabel('姓名')
pyplot.ylabel('战力值')
# 给图表添加标题、x轴标签、y轴标签




print('柱状图绘制中...')
pyplot.show()
