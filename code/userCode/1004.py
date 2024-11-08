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

def draw():
    bg1.draw()
    bg2.draw()
    bird.draw()

def update():
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
        # 判断角色 bird 是否飞出窗口顶端
        if bird.y>35:
            bird.y -= 5
    else:
        # 判断角色 bird 是否飞出窗口底部
        if bird.y<465:
            bird.y += 5

music.play('bgmusic')
pgzrun.go()