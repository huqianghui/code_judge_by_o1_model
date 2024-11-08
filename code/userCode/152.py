import pgzrun

WIDTH = 700
HEIGHT = 100

# 初始地图
map1 = [0, 1, 0, 0, 0, 0, 2]

# 创建角色
tiles = []
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
    # 编写if语句, 限制乌拉乎在地图中移动
    if action == 'left':
        if   i>0      :
            map1[i-1] = 1
            map1[i] = 0
    elif action == 'right':
        if  i<len(map1)-1       :
            map1[i+1] = 1
            map1[i] = 0
    print(map1)
    tiles = []
    create()

pgzrun.go()