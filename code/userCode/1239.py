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
# 创建岩浆角色
magma = Actor('岩浆1')
magma.x = 500
magma.y = 480


def draw():
    bg1.draw()
    bg2.draw()
    bird.draw()
    # 绘制岩浆
    magma.draw()


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
    # 切换月月鸟造型
    if bird.image == '月月鸟1':
        bird.image = '月月鸟2'
    else:
        bird.image = '月月鸟1'
    # 切换岩浆造型
    if magma.image == '岩浆1':
        magma.image = '岩浆2'
    else:
        magma.image = '岩浆1'
    
    
    
    
music.play('bgmusic')      
pgzrun.go()