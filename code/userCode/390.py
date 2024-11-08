import pgzrun

WIDTH = 600
HEIGHT = 600

ship = Actor('战舰')
ship.x = 300
ship.y = 100


def draw():
    screen.blit('太空', [0, 0])
    ship.draw()


def update():
    ship.y +1



pgzrun.go()
