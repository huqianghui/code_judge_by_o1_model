import pgzrun, random

WIDTH = 1000
HEIGHT = 500
bg1 = Actor('背景图1')
bg1.x = 500
bg1.y = 250
bg2 = Actor('背景图2')
bg2.x = bg1.x + 1000
bg2.y = 250
bird = Actor('月月鸟1')
bird.x = 200
bird.y = 100
magma = Actor('岩浆1')
magma.x = 500
magma.y = 480
b1 = Actor('藤蔓')
b1.x = 1000
b1.y = 100
b2 = Actor('枝干')
b2.x = 1600
b2.y = 75
b3 = Actor('尖刺')
b3.x = 2100
b3.y = 400

blocks = [b1, b2, b3]
names = ['藤蔓', '枝干', '尖刺']
num = [100, 75, 400]


def draw():
    bg1.draw()
    bg2.draw()
    bird.draw()
    magma.draw()
    for b in blocks:
        b.draw()


# 1.定义一个全局变量存储分数
score = 0


def update():
    # 2.声明全局变量score
    global score
    bg1.x -= 7
    bg2.x -= 7
    if bg1.x < -500:
        bg1.x = bg2.x + 1000
    if bg2.x < -500:
        bg2.x = bg1.x + 1000
    if bird.image == '月月鸟1':
        bird.image = '月月鸟2'
    else:
        bird.image = '月月鸟1'
    if keyboard.space:
        if bird.y > 35:
            bird.y -= 5
    else:
        if bird.y < 465:
            bird.y += 5
    if magma.image == '岩浆1':
        magma.image = '岩浆2'
    else:
        magma.image = '岩浆1'

    for b in blocks:
        b.x -= 7
        if b.x < -30:
            b.x = 1500
            n = random.randint(0, 2)
            b.image = names[n]
            b.y = num[n]
            # 3.分数score增大1
            score += 1
            print(score)

        if bird.colliderect(b):
            print('碰到障碍物')
            exit()

    if bird.colliderect(magma):
        print('碰到岩浆')
        exit()


music.play('bgmusic')
pgzrun.go()
