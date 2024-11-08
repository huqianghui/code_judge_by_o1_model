import pgzrun, random

WIDTH = 1000
HEIGHT = 500

score = 0

names = ['藤蔓', '枝干', '尖刺']
num = [100, 75, 400]
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
b1.type = names.index(b1.image)
b2 = Actor('枝干')
b2.x = 1600
b2.y = 75
b2.type = names.index(b2.image)
b3 = Actor('尖刺')
b3.x = 2100
b3.y = 400
b3.type = names.index(b3.image)

blocks = [b1, b2, b3]

def draw():
    global score
    bg1.draw()
    bg2.draw()
    bird.draw()
    magma.draw()
    for b in blocks:
        b.draw()
    screen.draw.text(str(score), (20, 10))

def update():
    state, reward, done = step(1)
    if done:
        print('游戏结束')
        
def step(action):
    global score
    state = None
    reward = 0
    done = False
    # 控制月月鸟向上或向下
    if action == 1:
        if bird.y > 35:
            bird.y -= 5
    else:
        if bird.y < 465:
            bird.y += 5
    # 切换造型
    if bird.image == '月月鸟1':
        bird.image = '月月鸟2'
    else:
        bird.image = '月月鸟1'
    if magma.image == '岩浆1':
        magma.image = '岩浆2'
    else:
        magma.image = '岩浆1'
    # 移动背景
    bg1.x -= 7
    bg2.x -= 7
    if bg1.x < -500:
        bg1.x = bg2.x + 1000
    if bg2.x < -500:
        bg2.x = bg1.x + 1000
    # 移动障碍物
    for b in blocks:
        b.x -= 7
        if b.x < -30:
            b.x = 1500
            n = random.randint(0, 2)
            b.type = n
            b.y = num[n]
            b.image = names[n]
            score += 1
            reward = 1

        if bird.colliderect(b):
            print('碰到障碍物')
            reward = -1
            dona=True

    if bird.colliderect(magma):
        print('碰到岩浆')
        reward = -1
        done=True
        

    # 得到月月鸟前方第一个障碍物的信息, 并存到first_b中
    first_b = blocks[0]
    for b in blocks:
        if (first_b.x < bird.x) or (b.x < first_b.x and b.x > bird.x):
            first_b = b
    # 设置状态
    state = [bird.y, first_b.x, first_b.y, first_b.type]

    return state, reward, done

music.play('bgmusic')
pgzrun.go()





