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
    bg1.draw()
    bg2.draw()

def update():
    bg1.x -= 7
    bg2.x -= 7
    # bg1 移出窗口左侧后, 拼接到 bg2 的右侧
    if bg1.x<-500:
        bg1.x=bg2.x+1000

    # bg2 移出窗口左侧后, 拼接到 bg1 的右侧
    if bg2.x<-500:
        bg2.x=bg1.x+1000


print('背景移动中, 请不要关闭游戏窗口')
music.play('bgmusic')
pgzrun.go()