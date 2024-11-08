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
    if key == keys.RIGHT:
        direction = '右'
    if key == keys.LEFT:
        direction = '左'
    # 按一下上键时, 传递信号 '上'
    if key == keys.UP:
        direction = '上'
    # 按一下下键时, 传递信号 '下'
    if key == keys.DOWN:
        direction = '下'


         
def update():
    global direction
    if direction == '右':
        bobo.x += 4
    if direction == '左':
        bobo.x -= 4
    # 接收到 '上' 信号后, 波波上移
    if direction == '上':
        bobo.y -= 4
    # 接收到 '下' 信号后, 波波下移
    if direction == '下':
        bobo.y += 4

pgzrun.go()