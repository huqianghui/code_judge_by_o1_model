import pgzrun

WIDTH = 600
HEIGHT = 600

bobo = Actor('波波')
bobo.x = 300
bobo.y = 300


def draw():
    screen.blit('奇妙岛', (0, 0))
    bobo.draw()


# 定义一个全局变量存储方向信号
direction = ''


def on_key_down(key):
    global direction
    # 按一下右键时, 传递信号
    if key == keys.RIGHT:
        direction = '右'

def update():
    global direction
    # 接收到信号后, 波波右移
    if direction == '右':
        bobo.x += 4


pgzrun.go()
