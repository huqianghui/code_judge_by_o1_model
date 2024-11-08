import pgzrun
import random

WIDTH = 500
HEIGHT = 700

#创建嘟嘟和5个踏板角色
dudu = Actor('嘟嘟')
bricks = []
for i in range(5):
    n = random.randint(1, 3)
    b = Actor('踏板' + str(n))
    min_x = b.width // 2
    max_x = WIDTH - b.width // 2
    b.x = random.randint(min_x, max_x)
    b.y = 140 * (i + 1)
    bricks.append(b)

    if i == 2:
        dudu.x = b.x
        dudu.bottom = b.top

def draw():
    screen.blit('背景', [0,0])
    dudu.draw()
    for b in bricks:
        b.draw()

def update():
    #====编写代码,使用方向键,控制嘟嘟左右移动====
    if keyboard.left:
        dudu.x -= 5
    if keyboard.right:
        dudu.x += 5




    #5个踏板重复向上移动
    for b in bricks:
        b.y -= 2
        if b.y < 0:
            b.y = HEIGHT
            n = random.randint(1, 3)
            b.image = '踏板' + str(n)
            min_x = b.width // 2
            max_x = WIDTH - b.width // 2
            b.x = random.randint(min_x, max_x)

    #嘟嘟跟随踏板移动
    for b in bricks:
        if b.colliderect(dudu):
            dudu.bottom = b.top





pgzrun.go()














