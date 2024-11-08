import pgzrun

WIDTH = 600
HEIGHT = 600

hole = Actor('虫洞')
hole.x = 30
hole.y = 100
barrier = Actor('障碍物')
barrier.x = 400
barrier.y = 20
barrier1 = Actor('障碍物1')
barrier1.x = 50
barrier1.y = 300
barrier2 = Actor('障碍物2')
barrier2.x = 350
barrier2.y = 450
ship = Actor('战舰')
ship.x = 500
ship.y = 400
airboat = Actor('飞船')
airboat.x = 0
airboat.y = 250


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
    if airboat.x > 600:
        airboat.x = 0
        



pgzrun.go()
