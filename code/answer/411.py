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

def draw():
    global state
    if state == 1:
        screen.blit('初始背景', (0, 0))
        start.draw()
    elif state == 2:
        screen.blit('运行背景', (0, 0))
        for b in blocks:
            b.draw()

target = 0

def on_mouse_down(pos):
    global state, target
    if start.collidepoint(pos):
        state = 2

    for b in blocks:
        if b.collidepoint(pos):
            # 如果点击正确的数字块
            if b.image == str(target):
                # 移除被点击的数字块
                blocks.remove(b)
                # 将应该点击的数字块编号增加 1
                target += 1

pgzrun.go()