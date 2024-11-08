import pgzrun

WIDTH = 500
HEIGHT = 500

hemu = Actor('禾木')

def draw():
    screen.clear()
    screen.blit('图灵小学', pos=[0, 0])
    hemu.draw()


pgzrun.go()
