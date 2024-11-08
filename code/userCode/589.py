import pgzrun

WIDTH = 500
HEIGHT = 700

bricks = []
for i in range(5):
    b = Actor('踏板1')
    # 设置踏板的竖直位置
    b.y=(i+1)*140
    bricks.append(b)

def draw():
    screen.blit('背景', [0, 0])
    for b in bricks:
        b.draw()

pgzrun.go()