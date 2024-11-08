hour = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
temp = [50, 48, 38, 20, 18, 11, 0, 7, 25, 29, 51, 49]
# 指定第4个区域绘制图表
pyplot.subplot(2, 2, 4)
# 使用plot()函数绘制折线图
pyplot.plot(hour, temp)
# 给折线图添加标题和坐标轴标签
pyplot.title('空间莲一天温度变化')
pyplot.xlabel('时间')
pyplot.ylabel('温度')

# 使用suptitle()函数添加总标题
pyplot.suptitle('空间莲信息')

print('图表绘制完成, 正在展示图表...')
pyplot.show()



