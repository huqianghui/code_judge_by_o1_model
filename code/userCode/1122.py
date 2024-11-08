import pgzrun

WIDTH = 700
HEIGHT = 100

# 初始地图
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

# 按键操作
def on_key_down(key):
    if key == keys.LEFT:
        step('left')
    if key == keys.RIGHT:
        step('right')

# 定义step()函数
# 根据参数action的值,修改列表map1
def step(action):
    # 取出乌拉乎角色当前位置
    i = map1.index(1)
    # 如果按下左键,让当前位置左侧的元素变为1,当前位置元素变为0
    if action == 'left':
        map1[i-1] = 1
        map1[i] = 0
    # 如果按下右键,让当前位置右侧的元素变为1,当前位置元素变为0
    if action=='right':
        map1[i+1]=1
        map1[i]=0
    



    print(map1)

pgzrun.go()





