from matplotlib import pyplot
pyplot.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'simhei']

name_data = [['王者荣耀', 97978],
             ['和平精英', 55671],
             ['迷你世界', 50053],
             ['我的世界', 50868],
             ['最强蜗牛', 24085],
             ['香肠派对', 22961],
             ['江南百景图', 14737],
             ['新神魔大陆', 19979],
             ['荒野乱斗', 19526],
             ['第五人格', 14556],
             ['欢乐斗地主', 8063],
             ['阴阳师', 12989],
             ['炉石传说', 8594],
             ['开心消消乐', 5342]]

def mykey(x):
    return x[1]

name_data.sort(key=mykey)

name = []
data = []
for n in name_data:
    name.append(n[0])
    data.append(n[1])

pyplot.title('游戏热度排行榜')
pyplot.xlabel('玩家人数')
pyplot.ylabel('游戏名称')
pyplot.barh(name, data)
print('水平柱状图绘制中...')
pyplot.show()