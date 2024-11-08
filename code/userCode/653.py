import pgzrun

WIDTH = 700
HEIGHT = 350

flag = 0
time = 0


taozi = Actor('桃子')
taozi.x = 100
taozi.y = 200

coin = Actor('金币')
coin.x = 600
coin.y = 300

def draw():
    screen.clear()
    screen.blit('背景', pos=[0, 0])
    taozi.draw()
    if flag == 0:
        coin.draw()

def update():
    global flag
    global time
    if taozi.colliderect(coin):
        flag = 1
    time += 1
    if time == 1200:
        flag = 3

def on_key_down():
    taozi.x=600
    taozi.y=200
    

pgzrun.go()
