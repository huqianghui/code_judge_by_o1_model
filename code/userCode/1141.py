import pgzrun
import random

WIDTH = 600
HEIGHT = 600

start = Actor('开始')
start.x = WIDTH / 2
start.y = 500

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
    # 如果游戏处于运行状态下
    if state == 2:
        # 将时间增加 1
        t +=1

# 让程序每秒钟调用一次tick()函数
clock.schedule_interval(tick,1)

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

target = 0

def on_mouse_down(pos):
    global state, target
    if start.collidepoint(pos):
        state = 2

    for b in blocks:
        if b.collidepoint(pos):
            if b.image == str(target):
                blocks.remove(b)
                target += 1

pgzrun.go()