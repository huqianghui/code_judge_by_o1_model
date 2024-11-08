import pgzrun
import random

WIDTH = 600
HEIGHT = 600

flag = 0

aim = Actor('瞄准状态')

enemy = Actor('正常状态')
enemy.x = random.randint(0, 600)
enemy.y = random.randint(0, 600)

submit = Actor('提交作业')

def draw():
    global  flag
    screen.clear()
    screen.blit('背景', pos = [0,0])
    enemy.draw()
    aim.draw()
    if flag == 1:
        submit.draw()

def on_mouse_move(pos):
    aim.pos = pos

def on_mouse_down():
    aim.image = '射击状态'
    if aim.colliderect(enemy):
        enemy.image = '被击中状态'

def on_mouse_up():
    aim.image = '瞄准状态'
    enemy.image = '正常状态'


    enemy.x = random.randint(0, 600)
    enemy.y = random.randint(0, 400)

pgzrun.go()
