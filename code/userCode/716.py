from matplotlib import pyplot

pyplot.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'simhei']

enemy = ['龙威', '龙心', '龙灵', '龙仁', '龙尔']
hemu = [90, 90, 80, 80, 40]
taozi = [80, 80, 70, 100, 85]

c = [1, 2, 3, 4, 5]
c1 = [i - 0.2 for i in c]
c2 = [i + 0.2 for i in c]

pyplot.bar(c1, hemu, width=0.4, color='skyblue')
pyplot.bar(c2, taozi, width=0.4, color='pink')

pyplot.title('战绩统计图')
pyplot.xlabel('智核星人')
pyplot.ylabel('战胜次数')
pyplot.legend(['禾木', '桃子'])

# 使用xticks()函数修改x轴显示的内容
pyplot.xticks(enemy,)





print('复式柱状图绘制中...')
pyplot.show()
