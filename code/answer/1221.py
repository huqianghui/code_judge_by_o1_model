import pgzrun

WIDTH = 600
HEIGHT = 600

start = Actor('开始')
start.x = WIDTH / 2
start.y = 500

def draw():
    screen.blit('初始背景', (0, 0))
    start.draw()

def on_mouse_down(pos):
    #====本关答案代码====
    if start.collidepoint(pos):
        print('游戏开始啦')


pgzrun.go()














