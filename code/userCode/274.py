from matplotlib import pyplot

pyplot.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'simhei']

grade = ['一年级', '二年级', '三年级', '四年级', '五年级', '六年级', '七年级', '八年级']
taozi = [120, 126, 132, 136, 142, 147, 155, 163]
pyplot.plot(grade,taozi)


print('折线图绘制中...')
pyplot.show()