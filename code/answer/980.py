import pgzrun

WIDTH = 600
HEIGHT = 600

hole = Actor('虫洞')
hole.x = 30
hole.y = 200
barrier = Actor('障碍物')
barrier.x = 500
barrier.y = 100
barrier1 = Actor('障碍物1')
barrier1.x = 150
barrier1.y = 50
barrier2 = Actor('障碍物2')
barrier2.x = 80
barrier2.y = 400
ship = Actor('战舰')
ship.x = 500
ship.y = 500
airboat = Actor('飞船')
airboat.x = 0
airboat.y = 300


def draw():
    screen.blit('太空', [0, 0])
    hole.draw()
    ship.draw()
    barrier.draw()
    barrier1.draw()
    barrier2.draw()
    airboat.draw()


def update():
    ship.y += 5

    if keyboard.space:
        ship.y -= 10
    if keyboard.left:
        ship.x -= 5
    if keyboard.right:
        ship.x += 5

    airboat.x += 3


pgzrun.go()
