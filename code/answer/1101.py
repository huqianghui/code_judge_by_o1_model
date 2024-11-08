from matplotlib import pyplot

pyplot.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'simhei']
enemy = ['龙威', '龙心', '龙灵', '龙仁', '龙尔']
hemu = [90, 90, 80, 80, 40]
taozi = [80, 80, 70, 100, 85]

pyplot.bar(enemy, taozi, width=0.4, color='pink')

pyplot.title('桃子战绩统计图')
pyplot.xlabel('智核星人')
pyplot.ylabel('战胜次数')

print('柱状图绘制中...')
pyplot.show()
