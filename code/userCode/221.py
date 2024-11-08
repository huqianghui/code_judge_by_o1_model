from matplotlib import pyplot

pyplot.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'simhei']

space = ['藤蔓林', '壁上草原', '中心区', '核心通道', '顶上草原', '入口']
risk = [10, 56, 73, 88, 33, 21]
pyplot.subplot(2, 2, 1)
pyplot.barh(space, risk)
pyplot.xlabel('危险指数')
pyplot.ylabel('区域名称')
pyplot.title('区域危险指数')

plants = ['大嘴花', '爆炸蘑菇', '弹弹蘑菇', '地笼草', '怪叫树']
num = [47, 31, 5, 8, 9]
pyplot.subplot(2, 2, 2)
pyplot.pie(num, labels=plants, autopct='%.1f%%')
pyplot.title('危险植物数量占比')

kind = ['α射线', 'β射线', 'γ射线', 'X射线', '声辐射', '引力辐射']
rad = [0.4, 0.6, 0.5, 0.8, 0.7, 1.2]
# 划分画布,指定第3个区域绘制图表
pyplot.subplot(2, 2, 3)
# 使用bar()函数绘制柱状图
pyplot.bar(kind, rad)
# 给柱状图添加标题和坐标轴标签
pyplot.xlabel('辐射类型')
pyplot.ylabel('辐射强度')
pyplot.title('核心通道辐射分布')


print('图表绘制完成, 正在展示图表...')
pyplot.show()