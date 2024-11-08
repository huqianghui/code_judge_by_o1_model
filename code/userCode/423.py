import pgzrun

WIDTH = 700
HEIGHT = 100

# 设计地图
map1 = [0, 1, 0, 0, 0, 0, 2]

# 创建角色
tiles = []
for i in range(len(map1)):
    if map1[i] == 0:
        tile = Actor('空地', (50+100*i, 50))
    elif map1[i] == 1:
        tile = Actor('乌拉乎', (50+100*i, 50))
    elif map1[i] == 2:
        tile = Actor('金币', (50+100*i, 50))
    tiles.append(tile)

# 绘制地图
def draw():
    for t in tiles:
        t.draw()

# 编写代码, 按下左键时, 打印'left', 按下右键时, 打印'right'
def on_key_down(key):
    if key==keys.LEFT:
        print('left')
    if key==keys.RIGHT:
        print('right')





pgzrun.go()