import pgzrun
import random

WIDTH = 500
HEIGHT = 700

player = Actor('小核桃')
player.x = 250
player.y = 650

weapons = []
bubus = []
for i in range(3):
    b = Actor('bubu')
    b.x = random.randint(0, 500)
    bubus.append(b)

def draw():
    screen.blit('星球', [0, 0])
    player.draw()
    
    for w in weapons:
        w.draw()
    for b in bubus:
        b.draw()

def update():
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5
   
    if keyboard.space:
        weapon = Actor('子弹')
        weapon.x = player.x
        weapon.y = player.y - 50
        weapons.append(weapon)
       
    for w in weapons:
        w.y -= 5
    for w in weapons:
        if w.y <= 0:
            weapons.remove(w)
    
    for b in bubus:
        b.y += 5
        #在这里编写代码,当bubu兽飞到窗口下边缘时,回到窗口上方
        if 


pgzrun.go()


