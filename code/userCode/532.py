# 本关无需编写代码, 直接运行即可
# 运行后, 按一下右键, 观察是否实现一直移动的效果

import pgzrun
WIDTH = 600
HEIGHT = 600

bobo = Actor('波波')
bobo.x = 300
bobo.y = 300

def draw():
    screen.blit('奇妙岛', (0, 0))
    bobo.draw()

def on_key_down(key):
    if key == keys.RIGHT:
        for i in range(50):
            bobo.x += 4

pgzrun.go()