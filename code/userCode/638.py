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

def on_mouse_down(pos):
    global state
    if start.collidepoint(pos):
        state = 2
    for b in blocks:
        # 使用if语句进行判断,如果数字块被点击,就打印该数字块的造型名称
        if b.collidepoint(pos):
            print(b.image)



pgzrun.go()





