from matplotlib import pyplot

pyplot.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'simhei']

names = ['禾木', '桃子', '乌拉乎', '麦杰', '麦琪']
points = [35, 35, 23, 32, 27]

# 使用bar()函数绘制柱状图并设置柱子的宽度和颜色
pyplot.bar(width=0.4,color='green')

pyplot.title('战斗力统计图')
pyplot.xlabel('姓名')
pyplot.ylabel('战力值')

print('柱状图绘制中...')
pyplot.show()
