from matplotlib import pyplot

pyplot.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'simhei']

grade = ['一年级', '二年级', '三年级', '四年级', '五年级', '六年级', '七年级', '八年级']
hemu = [125, 129, 138, 141, 145, 150, 159, 165]
wulahu = [129, 134, 136, 143, 146, 149, 157, 163]

pyplot.plot(grade, hemu)
pyplot.plot(grade, wulahu)
pyplot.legend('禾木','乌拉乎')


pyplot.title('身高变化折线图')
pyplot.xlabel('年级')
pyplot.ylabel('身高')

print('折线图绘制中...')
pyplot.show()