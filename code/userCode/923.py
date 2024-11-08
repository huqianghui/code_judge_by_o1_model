import pgzrun

WIDTH = 1000
HEIGHT = 500

# 创建角色 bg1 并设置初始坐标
b = Actor('bg1')
b.x = 500
b.y = 250



def draw():
    # 绘制角色 bg1
    bg1.draw()


music.play('bgmusic')
pgzrun.go()
