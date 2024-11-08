import pandas
from matplotlib import pyplot
pyplot.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'simhei']

data = pandas.read_csv('活动费用记录.csv')
num= data['人数']
money = data['费用']

pyplot.scatter(num, money)
print('散点图绘制中...')
pyplot.show()