import pgzrun
import random

WIDTH = 500
HEIGHT = 700

#创建小核桃
player = Actor('小核桃')
player.x = 250
player.y = 650

weapons = []
#创建3个bubu兽角色
bubus = []
for i in range(3):
    b = Actor('bubu')
    b.x = random.randint(0, 500)
    bubus.append(b)

def draw():
    screen.blit('星球', [0, 0])
    player.draw()
    #游戏失败之前绘制角色
    if player.image != '小核桃失败':
        for w in weapons:
            w.draw()
        for b in bubus:
            b.draw()
    else:
        screen.blit('提交作业', [0, 0])

def update():
    #小核桃移动
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5
    #空格键发射子弹    
    if keyboard.space:
        weapon = Actor('子弹')
        weapon.x = player.x
        weapon.y = player.y - 50
        weapons.append(weapon)
    
    #子弹从下向上移动，到窗口上边缘消失    
    for w in weapons:
        w.y -= 5
    for w in weapons:
        if w.y <= 0:
            weapons.remove(w)
    
    # bubu兽从上向下移动，到窗口下边后初始化到窗口上方
    for b in bubus:
        b.y += 5
        if b.y > 700:
            b.x = random.randint(0, 500)
            b.y = 0
    
    #bubu兽和子弹碰撞后，回到初始位置
    for b in bubus:
        for w in weapons:
            if b.colliderect(w):
                b.x = random.randint(0, 500)
                b.y = 0
        
        #bubu碰到小核桃游戏失败       
        if b.colliderect(player):
            player.image = '小核桃失败'
            #停止音乐
            music.stop()

#播放背景音乐
music.play('music1')
pgzrun.go()
