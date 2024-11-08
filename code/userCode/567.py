import pgzrun
import random

WIDTH = 500
HEIGHT = 700

dudu = Actor('嘟嘟')

bricks = []
for i in range(5):
    n = random.randint(1, 4)
    b = Actor('踏板' + str(n))
    min_x = b.width // 2
    max_x = WIDTH - b.width // 2
    b.x = random.randint(min_x, max_x)
    b.y = 140 * (i + 1)
    bricks.append(b)
    if i == 2:
        dudu.x = b.x
        dudu.bottom = b.top
        b.image = '踏板1'

def draw():
    screen.blit('背景', [0, 0])
    dudu.draw()
    for brick in bricks:
        brick.draw()

def update():
    on_brick = 0
    for b in bricks:
        b.y -= 3
        if b.y < 0:
            n = random.randint(1, 4)
            b.image = '踏板' + str(n)
            b.y = HEIGHT
            min_x = b.width // 2
            max_x = WIDTH - b.width // 2
            b.x = random.randint(min_x, max_x)
    for b in bricks:
        if dudu.colliderect(b) and dudu.bottom < b.bottom:
            dudu.bottom = b.top
            on_brick = 1
            # 当 dudu 踩到'踏板4'时, 造型切换为 '嘟嘟哭'
            if b.image == '踏板4':
                dudu.image = '嘟嘟哭'

    if on_brick == 0:
        dudu.y += 8
    if keyboard.left:
        if dudu.left > 0:
            dudu.x -= 5
    if keyboard.right:
        if dudu.right < WIDTH:
            dudu.x += 5

pgzrun.go()