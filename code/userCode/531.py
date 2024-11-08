import pgzrun
import random

WIDTH = 600
HEIGHT = 600

start = Actor('开始')
start.x = WIDTH / 2
start.y = 500


num = [10, 6, 13, 3, 4, 5, 1, 7, 15, 9, 0, 11, 12, 2, 14, 8]
#===编写代码,打乱列表num顺序===
random.shuffle(num)

blocks = []
index = 0
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
    #根据游戏状态绘制不同内容
    if state == 1:
        screen.blit('初始背景', (0, 0))
        start.draw()
    elif state == 2:
        screen.blit('运行背景', (0, 0))
        for b in blocks:
            b.draw()

#鼠标点击'开始游戏'按钮
def on_mouse_down(pos):
    global state
    if start.collidepoint(pos):
        state = 2


pgzrun.go()

