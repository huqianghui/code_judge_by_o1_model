import pgzrun

WIDTH = 300
HEIGHT = 500

flag = 0
time = 0

wulahu = Actor('乌拉乎')
wulahu.y = 407

fail = Actor('闯关失败')
fail.x = 150
fail.y = 100

success = Actor('闯关成功')
success.x = 150
success.y = 100

def draw():
    global flag
    screen.clear()
    screen.blit('草原', pos=[0, 0])
    wulahu.draw()
    if flag == 1:
        fail.draw()
    if flag == 2:
        success.draw()

def update():
    global flag
    global time
    if wulahu.x >= 260:
        flag = 2
    time += 1
    if time == 1200:
        flag = 3


def on_key_down():
    wulahu.x += 20


pgzrun.go()
