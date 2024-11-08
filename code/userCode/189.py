from matplotlib import pyplot
import pandas

pyplot.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'simhei']
pyplot.figure(figsize=(14, 4))

# 读取 '足迹实验.csv' 文件中的数据
data = pandas.read_csv('足迹实验.csv')
# 取出 '鞋印长度' 数据
shoe = data['鞋印长度']
# 取出 '深度' 数据
depth = data['深度']
# 取出 '步长' 数据
step = data['步长']
# 取出 '身高' 数据
height = data['身高']

# 绘制鞋印长度与身高的散点图
pyplot.subplot(1, 3, 1)
pyplot.title('鞋印长度与身高散点图')
pyplot.scatter(shoe,height)

# 绘制深度与身高的散点图
pyplot.subplot(1, 3, 2)
pyplot.title('深度与身高散点图')
pyplot.scatter(depth,height)


# 绘制步长与身高的散点图
pyplot.subplot(1, 3, 3)
pyplot.title('步长与身高散点图')
pyplot.scatter(step,height)


print('图表绘制中...')
pyplot.show()
