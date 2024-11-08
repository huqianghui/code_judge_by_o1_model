import pgzrun

WIDTH = 500
HEIGHT = 700

bricks = []
for i in range(5):
    b = Actor('踏板1')
    b.y = 140 * (i + 1)
    bricks.append(b)

def draw():
    screen.blit('背景', [0, 0])
    for b in bricks:
        b.draw()

pgzrun.go()