import pgzrun
import random

WIDTH = 700
HEIGHT = 500

wulahu = Actor('乌拉乎')
wulahu.x = 50
wulahu.y = 50
point = Actor('安全点开启')
point.x = 650
point.y = 450
enemy = [Actor('守护者0左', [670, 30]), Actor('墨玉0左', [30, 470]), Actor('杜昀0左', [170, 470])]


def draw():
    screen.blit('公园a', [0, 0])
    point.draw()
    wulahu.draw()
    for i in enemy:
        i.draw()


def on_key_down(key):
    if key == keys.RIGHT:
        wulahu.x += 50
    if key == keys.DOWN:
        wulahu.y += 50


flag = 1
step = 0
names = ['守护者', '墨玉', '杜昀']


def update():
    global flag, step
    if flag == 1:
        if wulahu.distance_to(point) < 30:
            flag = 2
    if wulahu.y > HEIGHT:
        wulahu.y = HEIGHT - 5
    if wulahu.y < 0:
        wulahu.y = 5
    if wulahu.x > WIDTH:
        wulahu.x = WIDTH - 5
    if wulahu.x < 0:
        wulahu.x = 5
    if flag == 1:
        for i in range(len(enemy)):
            if enemy[i].colliderect(wulahu):
                flag = 0
            if enemy[i].x <= wulahu.x:
                enemy[i].image = names[i] + str(step) + '右'
                step += 1
                if step > 4:
                    step = 0
                enemy[i].x += 0.6
            elif enemy[i].x > wulahu.x:
                enemy[i].image = names[i] + str(step) + '左'
                step += 1
                if step > 4:
                    step = 0
                enemy[i].x -= 0.6
            if enemy[i].y < wulahu.y:
                enemy[i].y += 0.6
            elif enemy[i].y > wulahu.y:
                enemy[i].y -= 0.6
            for j in enemy:
                if enemy[i].colliderect(j):
                    if enemy[i] != j:
                        enemy[i].x += random.randint(0, 2)
                        j.x -= random.randint(0, 2)
                        enemy[i].y -= random.randint(0, 2)
                        j.y += random.randint(0, 2)


pgzrun.go()
