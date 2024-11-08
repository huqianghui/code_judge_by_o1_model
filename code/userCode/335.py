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
pyplot.subplot(2, 2, 3)
pyplot.bar(kind, rad)
pyplot.xlabel('辐射类型')
pyplot.ylabel('辐射强度')
pyplot.title('核心通道辐射分布')

# 时间
hour = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
# 温度
temp = [50, 48, 38, 20, 18, 11, 0, 7, 25, 29, 51, 49]
# 指定第4个区域绘制图表
pyplot.subplot(2,2,4)
# 使用plot()函数绘制折线图
pyplot.plot(hour,temp)
# 给折线图添加标题和坐标轴标签
pyplot.title('空间莲一天温度变化')
pyplot.xlabel('时间')
pyplot.ylabel('温度')

# 使用suptitle()函数添加总标题
pyplot.suptitle('空间莲信息')

print('图表绘制完成, 正在展示图表...')
pyplot.show()



