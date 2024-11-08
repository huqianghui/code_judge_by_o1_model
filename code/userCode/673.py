import pgzrun

WIDTH = 500
HEIGHT = 700

player = Actor('小核桃')
player.x = 250
player.y = 650

# 创建一个空列表, 用来存储多枚子弹
weapons = []
def draw():
    screen.blit('星球', [0, 0])
    player.draw()
    # 遍历存储子弹的列表, 让所有子弹显示出来
for i in weapons:
    i.draw()
def on_key_down(key):
    if key == keys.LEFT:
        player.x -= 20
    if key == keys.RIGHT:
        player.x += 20
    if key == keys.UP:
        player.y -= 20
    if key == keys.DOWN:
        player.y += 20
    # 创建子弹角色后, 使用append()把角色添加到列表中
    # 使用格式: 列表.append(新元素)
    if key == keys.SPACE:
        weapon = Actor('子弹')
        weapon.x = player.x
        weapon.y = player.y
        weapons.append(weapon)


pgzrun.go()