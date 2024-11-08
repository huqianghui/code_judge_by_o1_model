import pgzrun

WIDTH = 600
HEIGHT = 600

hole = Actor('虫洞')
hole.x = 570
hole.y = 150
barrier = Actor('障碍物')
barrier.x = 100
barrier.y = 50
barrier1 = Actor('障碍物1')
barrier1.x = 50
barrier1.y = 450
barrier2 = Actor('障碍物2')
barrier2.x = 450
barrier2.y = 300
ship = Actor('战舰')
ship.x = 500
ship.y = 500


def draw():
    screen.blit('太空', [0, 0])
    hole.draw()
    barrier.draw()
    barrier1.draw()
    barrier2.draw()
    ship.draw()


def update():
    ship.y += 5

    if keyboard.space:
        ship.y -= 10
    if keyboard.left:
        ship.x -= 5
    if keyboard.right:
        ship.x += 5


pgzrun.go()
