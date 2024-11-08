from matplotlib import pyplot

#windows系统字体: 'simhei' 
#苹果电脑使用: 'Arial Unicode MS'
pyplot.rcParams['font.sans-serif'] = 'simhei'

data = [950, 5390, 610, 3130]
lab = ['学编程', '打怪兽', '吃饭', '睡觉']
pyplot.pie(data, labels=lab)

print('稍等片刻,饼图马上就出来啦...')
pyplot.show()