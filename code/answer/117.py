import pgzrun

WIDTH = 1000
HEIGHT = 500

bg1 = Actor('背景图1')
bg1.x = 500
bg1.y = 250

# 创建角色 bg2 并设置初始坐标
bg2 = Actor('背景图2')
bg2.x = bg1.x + 1000
bg2.y = 250

def draw():
    bg1.draw()
    # 绘制角色 bg2
    bg2.draw()

music.play('bgmusic')
pgzrun.go()