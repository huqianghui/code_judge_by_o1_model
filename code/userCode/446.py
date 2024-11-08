import pgzrun

WIDTH = 700
HEIGHT = 350

flag = 0
time = 0

taozi = Actor('桃子')
taozi.x = 50
taozi.y = 200

coins = []
for i in range(3):
    coin = Actor('金币')
    coin.x = (i+1) * 200
    coin.y = 280
    coins.append(coin)

def draw():
    screen.clear()
    screen.blit('背景', pos=[0, 0])
    for c in coins:
        c.draw()
    taozi.draw()

def update():
    global flag
    global time
    for c in coins:
        if taozi.colliderect(c):
            coins.remove(c)
    if len(coins) == 0:
        flag = 1
    time += 1
    if time == 1200:
        flag = 2

def on_key_down():
    taozi.x + 50


pgzrun.go()   
