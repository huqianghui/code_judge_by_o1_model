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
        screen.blit('结束背景', (0, 0))
        restart.draw()
        screen.draw.text(str(t), (272, 300), fontsize=100, color='white')

target = 0

def on_mouse_down(pos):
    global state, target, t, blocks
    # 当游戏处于初始状态下, 鼠标点击开始按钮, 才可以启动游戏
    if start.collidepoint(pos) and state==1:
        state = 2

    for b in blocks:
        # 当游戏处于运行状态下, 鼠标点击正确的数字块, 才可以让数字块消失
        if b.collidepoint(pos) and state==2:
            if b.image == str(target):
                blocks.remove(b)
                target += 1
                if len(blocks) == 0:
                    state = 0
            else:
                t += 2

    # 当游戏处于结束状态下, 鼠标点击重新开始按钮, 才可以重新开始游戏
    if restart.collidepoint(pos) and state==0:
        state = 2
        random.shuffle(num)
        index = 0
        blocks = []
        target = 0
        t = 0
        for r in range(4):
            for c in range(4):
                n = str(num[index])
                b = Actor(n)
                b.x = 180 + c * 80
                b.y = 180 + r * 80
                blocks.append(b)
                index += 1

pgzrun.go()