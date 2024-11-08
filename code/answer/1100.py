import pgzrun

WIDTH = 500
HEIGHT = 700

player = Actor('小核桃')
player.x = 250
player.y = 650

weapons = []


def draw():
    screen.blit('星球', [0, 0])
    player.draw()
    for w in weapons:
        w.draw()


def on_key_down(key):
    if key == keys.LEFT:
        player.x -= 20
    if key == keys.RIGHT:
        player.x += 20
    if key == keys.UP:
        player.y -= 20
    if key == keys.DOWN:
        player.y += 20

    if key == keys.SPACE:
        weapon = Actor('子弹')
        weapon.x = player.x
        weapon.y = player.y - 60
        weapons.append(weapon)


def update():
    for w in weapons:
        w.y -= 5
    for w in weapons:
        if w.y <= 0:
            weapons.remove(w)


pgzrun.go()