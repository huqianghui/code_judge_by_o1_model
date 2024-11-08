import pgzrun

WIDTH = 1000
HEIGHT = 500

bg1 = Actor('背景图1')
bg1.x = 500
bg1.y = 250

bg2 = Actor('背景图2')
bg2.x = bg1.x + 1000
bg2.y = 250

def draw():
    screen.clear()
    bg1.draw()
    bg2.draw()

def update():
    # 减小角色的x坐标, 让角色 bg1 和 bg2 向左移动



print('背景移动中, 请不要关闭游戏窗口')
music.play('bgmusic')
pgzrun.go()