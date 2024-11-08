import pgzrun
import random

WIDTH = 700
HEIGHT = 500

taozi = Actor('桃子')
taozi.x = 600
taozi.y = 250
point = Actor('安全点关闭')
point.x = 50
point.y = 120
button = Actor('按钮')
button.x = 400
button.y = 120
enemy = [Actor('墨玉0左', [650, 50]), Actor('杜昀0左', [50, 450]), Actor('铃黄0左', [150, 480])]

def draw():
    screen.blit('广场', [0, 0])
    button.draw()
    point.draw()
    taozi.draw()
    for i in enemy:
        i.draw()


def on_key_down(key):
    if key == keys.RIGHT:
        taozi.x += 50
    if key == keys.DOWN:
        taozi.y += 50
    if key == keys.UP:
        taozi.y -= 50
    if key == keys.LEFT:
        taozi.x -= 50


    c = taozi.colliderect(button)
    if c == True:
        button.image = '按钮按下'






flag = 1
step = 0

names = ['墨玉', '杜昀', '铃黄']


def update():
    global flag, step
    if flag == 1:
        if taozi.distance_to(point) < 30 and point.image == '安全点开启':
            flag = 2
        if taozi.y > HEIGHT:
            taozi.y = HEIGHT - 5
        if taozi.y < 0:
            taozi.y = 5
        if taozi.x > WIDTH:
            taozi.x = WIDTH - 5
        if taozi.x < 0:
            taozi.x = 5
    if flag == 1:
        for i in range(3):
            if enemy[i].colliderect(taozi):
                flag = 0
            if enemy[i].x < taozi.x:
                enemy[i].image = names[i] + str(step) + '右'
                step += 1
                if step > 4:
                    step = 0
                enemy[i].x += 0.6
            else:
                enemy[i].image = names[i] + str(step) + '左'
                step += 1
                if step > 4:
                    step = 0
                enemy[i].x -= 0.6
            if enemy[i].y < taozi.y:
                enemy[i].y += 0.6
            else:
                enemy[i].y -= 0.6
            for j in enemy:
                if enemy[i].colliderect(j):
                    if enemy[i] != j:
                        enemy[i].x += random.randint(0, 2)
                        j.x -= random.randint(0, 2)
                        enemy[i].y -= random.randint(0, 2)
                        j.y += random.randint(0, 2)


pgzrun.go()
