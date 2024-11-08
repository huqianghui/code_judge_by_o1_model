import pgzrun

WIDTH = 500
HEIGHT = 700

# 定义draw()函数, 使用screen.blit()在窗口中显示背景图
def draw():
    screen.blit('星球',[0,0])
pgzrun.go()