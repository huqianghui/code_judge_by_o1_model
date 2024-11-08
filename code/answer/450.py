kind = ['α射线', 'β射线', 'γ射线', 'X射线', '声辐射', '引力辐射']
rad = [0.4, 0.6, 0.5, 0.8, 0.7, 1.2]
# 指定第3个区域绘制图表
pyplot.subplot(2, 2, 3)
# 使用bar()函数绘制柱状图
pyplot.bar(kind, rad)
# 给柱状图添加标题和坐标轴标签
pyplot.xlabel('辐射类型')
pyplot.ylabel('辐射强度')
pyplot.title('核心通道辐射分布')

print('图表绘制完成, 正在展示图表...')
pyplot.show()