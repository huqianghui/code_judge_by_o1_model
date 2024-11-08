import pgzrun
import random

WIDTH = 600
HEIGHT = 600

bobo = Actor('波波')
bobo.x = 300
bobo.y = 300

ball = Actor('能量球')
ball.x = random.randint(ball.width // 2, WIDTH - ball.width // 2)
ball.y = random.randint(ball.height // 2, HEIGHT - ball.height // 2)

direction = ''
score = 0  # 初始化分数


def draw():
    # 声明全局变量
    global score

    screen.blit('奇妙岛', (0, 0))
    bobo.draw()
    ball.draw()
    # 显示分数
    screen.draw.text(str(score), (10, 10))

def update():
    # 声明全局变量
    global direction

    if direction == '上' and bobo.top > 0:
        bobo.y -= 4
    elif direction == '下' and bobo.bottom < HEIGHT:
        bobo.y += 4
    elif direction == '左' and bobo.left > 0:
        bobo.x -= 4
    elif direction == '右' and bobo.right < WIDTH:
        bobo.x += 4

    if bobo.colliderect(ball):
        ball.x = random.randint(ball.width // 2, WIDTH - ball.width // 2)
        ball.y = random.randint(ball.height // 2, HEIGHT - ball.height // 2)
        # 收集到能量球加1分
        score += 1


def on_key_down(key):
    global direction

    if key == keys.UP:
        direction = '上'
    if key == keys.DOWN:
        direction = '下'
    if key == keys.LEFT:
        direction = '左'
    if key == keys.RIGHT:
        direction = '右'


pgzrun.go()