from matplotlib import pyplot

pyplot.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'simhei']

enemy = ['龙威', '龙心', '龙灵', '龙仁', '龙尔']
hemu = [90, 90, 80, 80, 40]
taozi = [80, 80, 70, 100, 85]

c = [1, 2, 3, 4, 5]
# 使用列表生成式计算禾木柱子的坐标
c1 = [i - 0.2 for i in c]
# 使用列表生成式计算桃子柱子的坐标
c2 = [i + 0.2 for i in c]
print(c2)
