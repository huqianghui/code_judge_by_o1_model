import pgzrun

WIDTH = 800
HEIGHT = 540

notice = Actor('提醒', (660, 50))
recog = Actor('识别', (660, 360))
clean = Actor('清除', (660, 460))


def draw():
    screen.draw.line((20, 20), (520, 20), 'brown')
    screen.draw.line((520, 20), (520, 520), 'brown')
    screen.draw.line((520, 520), (20, 520), 'brown')
    screen.draw.line((20, 520), (20, 20), 'brown')

    clean.draw()
    recog.draw()
    notice.draw()


def on_mouse_move(pos, buttons):
    # ===========在下面编写代码===========
    # 如果按下了鼠标左键, 就打印出当前的鼠标坐标
    if mouse.LEFT in buttons:
    
        print(pos)


pgzrun.go()