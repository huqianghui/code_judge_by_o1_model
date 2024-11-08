import pgzrun

WIDTH = 600
HEIGHT = 600

hole = Actor('虫洞')
hole.x = 30
hole.y = 100
barrier = Actor('障碍物')
barrier.x = 100
barrier.y = 300
barrier1 = Actor('障碍物1')
barrier1.x = 500
barrier1.y = 50
ship = Actor('战舰')
ship.x = 400
ship.y = 200
airboat = Actor('飞船')
airboat.x = 0
airboat.y = 200
airboat2 = Actor('飞船2')
airboat2.x = 0
airboat2.y = 450


def draw():
    screen.blit('太空', [0, 0])
    hole.draw()
    ship.draw()
    barrier.draw()
    barrier1.draw()
    airboat.draw()
    airboat2.draw()


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

    airboat2.x += 5
    if airboat2.x > 600:
        airboat2.x = 0

    if airboat.colliderect(ship):
        ship.image = '破损的战舰'

    if airboat2.colliderect(ship):
        ship.image = '破损的战舰'


pgzrun.go()
