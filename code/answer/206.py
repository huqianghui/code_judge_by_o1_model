from matplotlib import pyplot
pyplot.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei']
names = ['赤洋', '金翼漠', '海岛', '中央岛', '酸浆林']
area = [8900, 16700, 21700, 35400, 53300]
num = [61, 68, 98, 135, 76]
pyplot.subplot(1, 2, 1)
pyplot.barh(names, area)
pyplot.xlabel('面积')
pyplot.ylabel('基地名称')
pyplot.title('面积统计图')
pyplot.subplot(1, 2, 2)
pyplot.pie(num, labels=names, autopct='%.1f%%')

# 添加子图标题
pyplot.title('输出改造生物数量占比图')
# 添加总标题
pyplot.suptitle('智核星生物基地信息图')

print('多子图绘制中...')
pyplot.show()
