from matplotlib import pyplot

#windows系统字体: 'simhei' 
#苹果电脑使用: 'Arial Unicode MS'
pyplot.rcParams['font.sans-serif'] = 'simhei'

data = [950, 5390, 610, 3130]
lab = ['学编程', '打怪兽', '吃饭', '睡觉']
#在pie()函数中添加参数
pyplot.pie(data, labels=lab,autopct='%.2f%%')

print('稍等片刻,饼图马上就出来啦...')
pyplot.show()