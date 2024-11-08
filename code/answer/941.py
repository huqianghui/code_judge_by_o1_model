num = [47, 31, 5, 8, 9]
plants = ['大嘴花', '爆炸蘑菇', '弹弹蘑菇', '地笼草', '怪叫树']
# 指定第2个区域绘制图表
pyplot.subplot(2, 2, 2)
# 绘制饼图
pyplot.pie(num, labels=plants, autopct='%.1f%%')
# 给饼图添加标题
pyplot.title('危险植物数量占比')

print('图表绘制完成, 正在展示图表...')
pyplot.show()