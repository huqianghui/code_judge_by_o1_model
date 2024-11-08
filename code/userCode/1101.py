from matplotlib import pyplot

pyplot.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'simhei']

enemy = ['龙威', '龙心', '龙灵', '龙仁', '龙尔']
hemu = [90, 90, 80, 80, 40]
taozi = [80, 80, 70, 100, 85]

# 使用bar()函数绘制柱状图并设置柱子的宽度和颜色
pyplot.ber(enemy,taozi,width = 0.4,color = 'pink')

# 给图表添加标题、x轴标签、y轴标签




print('柱状图绘制中...')
pyplot.show()
