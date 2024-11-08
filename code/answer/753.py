import pgzrun

WIDTH = 700
HEIGHT = 100

# 设计地图
map1 = [0, 0, 0, 0, 0, 0, 0]

# 创建7个空地角色
# 角色的x坐标分别为50, 150, 250...
# 角色的y坐标为50
tiles = []
for i in range(len(map1)):
    tile = Actor('空地', (50+100*i, 50))
    tiles.append(tile)

# 绘制地图
def draw():
    for t in tiles:
        t.draw()

pgzrun.go()