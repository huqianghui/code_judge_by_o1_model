import pgzrun

WIDTH = 600
HEIGHT = 600

start = Actor('开始')
start.x = WIDTH / 2
start.y = 500

state = 1 #state为1表示初始状态

def draw():
    global state
    #====本关答案代码====
    if state == 1:
        screen.blit('初始背景', (0, 0))
        start.draw()
    elif state == 2:
        screen.blit('运行背景', (0, 0))


#鼠标点击'开始游戏'按钮
def on_mouse_down(pos):
    global state
    if start.collidepoint(pos):
        state = 2 #state为2表示运行状态

pgzrun.go()















