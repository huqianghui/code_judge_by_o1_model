from matplotlib import pyplot
pyplot.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'simhei']

name = ['王者荣耀', '香肠派对', '我的世界', '第五人格', '和平精英']
data = [97978, 22961, 50868, 14556, 55671]
pyplot.bar(name, data)

print('柱状图绘制中...')
pyplot.show()

