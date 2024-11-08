import pgzrun

WIDTH = 1000
HEIGHT = 500

# 创建角色 bg1 并设置初始坐标
bg1=Actor('背景图1')





def draw():
    # 绘制角色 bg1
    bg1.draw()


music.play('bgmusic')
pgzrun.go()
