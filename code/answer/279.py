import pgzrun

WIDTH = 600
HEIGHT = 600

hole = Actor('虫洞')
hole.x = 300
hole.y = 20
ship = Actor('战舰')
ship.x = 300
ship.y = 300


def draw():
    screen.blit('太空', [0, 0])
    hole.draw()
    ship.draw()


def update():
    ship.y += 5


def on_key_down(key):
    if key == keys.SPACE:
        ship.y -= 100


pgzrun.go()
