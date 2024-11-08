import pgzrun
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

# 创建障碍物角色
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


def draw():
    bg1.draw()
    bg2.draw()
    bird.draw()
    magma.draw()
    # 遍历blocks, 将每个障碍物绘制出来
    for i in blocks:
        i.draw()
        

    

def update():
    bg1.x -= 7
    bg2.x -= 7
    if bg1.x < -500:
        bg1.x = bg2.x + 1000
    if bg2.x < -500:
        bg2.x = bg1.x + 1000
    if keyboard.space:
        if bird.y > 35:
            bird.y -= 5
    else:
        if bird.y < 465:
            bird.y += 5
    if bird.image == '月月鸟1':
        bird.image = '月月鸟2'
    else:
        bird.image = '月月鸟1'
    if magma.image == '岩浆1':
        magma.image = '岩浆2'
    else:
        magma.image = '岩浆1'
    # 遍历blocks, 让每个障碍物向左移动
    for i in blocks:
        i.x -= 7

    
music.play('bgmusic')
pgzrun.go()