import pgzrun
import random

WIDTH = 600
HEIGHT = 600

start = Actor('开始')
start.x = WIDTH / 2
start.y = 500

restart = Actor('重新开始')
restart.x = WIDTH / 2
restart.y = HEIGHT / 2 + 200

num = []
for i in range(16):
    num.append(i)
random.shuffle(num)

index = 0
blocks = []
for r in range(4):
    for c in range(4):
        n = str(num[index])
        b = Actor(n)
        b.x = 180 + c * 80
        b.y = 180 + r * 80
        blocks.append(b)
        index += 1

state = 1

t = 0
def tick():
    global t, state
    if state == 2:
        t += 1

clock.schedule_interval(tick, 1)

def draw():
    global state, t
    if state == 1:
        screen.blit('初始背景', (0, 0))
        start.draw()
    elif state == 2:
        screen.blit('运行背景', (0, 0))
        for b in blocks:
            b.draw()
        screen.draw.text(str(t), (308, 52), fontsize=48, color='purple')
    elif state == 0:
        # 显示'结束背景'
        screen.blit('结束背景',(0,0))
        # 绘制 restart 重新开始按钮
        restart.draw()
        screen.draw.text(str(t), (272, 300), fontsize=100, color='white')

target = 0

def on_mouse_down(pos):
    global state, target, t
    if start.collidepoint(pos):
        state = 2

    for b in blocks:
        if b.collidepoint(pos):
            if b.image == str(target):
                blocks.remove(b)
                target += 1
                if len(blocks) == 0:
                    state = 0
            else:
                t += 2

pgzrun.go()
