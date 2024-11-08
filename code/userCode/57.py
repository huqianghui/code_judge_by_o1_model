from matplotlib import pyplot
pyplot.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'simhei']

name_data = [['王者荣耀', 97978],
             ['香肠派对', 22961],
             ['我的世界', 50868],
             ['第五人格', 14556],
             ['和平精英', 55671]]

def mykey(x):
    return x[1]

name_data.sort(key=mykey)
#编写代码,分别将游戏名称和玩家人数添加到列表name和data中
name = []
data = []
for i in name_data:
    name.append(i[0])
    data.append(i[1])


pyplot.bar(name, data)
print('柱状图绘制中...')
pyplot.show()












