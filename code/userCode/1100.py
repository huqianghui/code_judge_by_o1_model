 import pgzrun

#设置窗口大小
WIDTH = 500
HEIGHT = 700

#创建角色
player = Actor('小核桃')
player.x = 250
player.y = 650

#创建列表存储多枚子弹
weapons = []


def draw():
    screen.blit('星球', [0, 0])
    player.draw()
    # 显示子弹
    for w in weapons:
        w.draw()


def on_key_down(key):
    # 方向键控制角色移动
    if key == keys.LEFT:
        player.x -= 20
    if key == keys.RIGHT:
        player.x += 20
    if key == keys.UP:
        player.y -= 20
    if key == keys.DOWN:
        player.y += 20

    # 空格键创建子弹角色
    if key == keys.SPACE:
        weapon = Actor('子弹')
        weapon.x = player.x
        weapon.y = player.y-60
        weapons.append(weapon)
        

def update():
    # 子弹射出
    for w in weapons:
        w.y -= 5
    # 子弹删除
    for w in weapons:
        if w.y <= 0:
            weapons.remove(w)
     

pgzrun.go()