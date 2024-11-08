import pgzrun

WIDTH = 600
HEIGHT = 600

aim = Actor('瞄准状态')
enemy = Actor('正常状态')

def draw():
    screen.clear()
    screen.blit('背景', pos = [0,0])
    enemy.draw()
    aim.draw()

def on_mouse_down():
    aim.image = '射击状态'
    if aim.colliderect(enemy):
        enemy.image = '被击中状态'

def on_mouse_up():
    aim.image = '瞄准状态'

def on_mouse_move(pos):
    aim.pos = pos

pgzrun.go()
