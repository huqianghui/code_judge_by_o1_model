import pgzrun
WIDTH = 600
HEIGHT = 600
 
bobo = Actor('波波')
# 设置波波的坐标
bobo.x = 300
bobo.y = 300
 
def draw():
    screen.blit('奇妙岛', (0, 0))
    # 将波波绘制出来
    bobo.draw()
 
pgzrun.go()