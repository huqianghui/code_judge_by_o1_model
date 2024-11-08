import pgzrun
import random

WIDTH = 500
HEIGHT = 700

dudu = Actor('嘟嘟')

score = 0

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
    global score
    screen.blit('背景', [0, 0])
    dudu.draw()
    for brick in bricks:
        brick.draw()
    screen.draw.text(str(score), (20, 10))

def update():
    global score
    if dudu.image == '嘟嘟':
        score += 1
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
                if b.image == '踏板4':
                    dudu.image = '嘟嘟哭'
        if on_brick == 0:
            dudu.y += 8
        if dudu.bottom > HEIGHT:
            dudu.image = '嘟嘟哭'
        if keyboard.left:
            if dudu.left > 0:
                dudu.x -= 5
        if keyboard.right:
            if dudu.right < WIDTH:
                dudu.x += 5

# 编写 on_key_down() 函数, 当游戏结束且玩家按下空格键时, 重新开始游戏D
def on_key_down(key):
    if key == keys.SPACE and dudu.image == '嘟嘟哭':
        

        global score, bricks
        dudu.image = '嘟嘟'
        bricks = []
        score = 0
        for i in range(5):
            n = random.randint(1, 4)
            b = Actor('踏板' + str(n))
            min_x = b.width // 2
            max_x = WIDTH - b.width // 2
            b.x = random.randint(min_x, max_x)
            b.y = 140 * (i + 1)
            bricks.append(b)
            if i == 2:
                b.image = '踏板1'
                dudu.x = b.x
                dudu.bottom = b.top

pgzrun.go()