import pgzrun
import random

WIDTH = 500
HEIGHT = 700

bricks = []
for i in range(5):
    n = random.randint(1, 3)
    b = Actor('踏板' + str(n))
    min_x = b.width // 2
    max_x = WIDTH - b.width // 2
    b.x = random.randint(min_x, max_x)
    b.y = 140 * (i + 1)
    bricks.append(b)

def draw():
    screen.blit('背景', [0, 0])
    for b in bricks:
        b.draw()
     
def update():
    for b in bricks:
        b.y -= 2

pgzrun.go()