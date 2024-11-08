import pgzrun

WIDTH = 700
HEIGHT = 100

# 初始地图
map1 = [0, 1, 0, 0, 0, 0, 2]

# 创建角色
tiles = []

# 定义create()函数, 根据列表map1创建对应的角色(0对应空地, 1对应乌拉乎, 2对应金币)
def create():
    for i in range(len(map1)):
        if map1[i] == 0:
            tile = Actor('空地', (50+100*i, 50))
        elif map1[i] == 1:
            tile = Actor('乌拉乎', (50+100*i, 50))
        elif map1[i] == 2:
            tile = Actor('金币', (50+100*i, 50))
        tiles.append(tile)

create()

# 绘制地图
def draw():
    for t in tiles:
        t.draw()

# 按键事件
def on_key_down(key):
    if key == keys.LEFT:
        step('left')
    if key == keys.RIGHT:
        step('right')

# 更新列表(环境)
def step(action):
    global tiles
    i = map1.index(1)
    if action == 'left':
        map1[i] = 0
        map1[i-1] = 1
    elif action == 'right':
        map1[i] = 0
        map1[i+1] = 1
    print(map1)
    tiles = []
    create()

pgzrun.go()