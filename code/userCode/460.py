import pgzrun

WIDTH = 300
HEIGHT = 500

flag = 0
step = 0
time = 0

wulahu = Actor('乌拉乎')
wulahu.y = 407

guard = Actor('沙漠守卫_左')
guard.x = 280
guard.y = 400
guard_move_left = ['沙漠守卫_走路左_0', '沙漠守卫_走路左_1', '沙漠守卫_走路左_2', '沙漠守卫_走路左_3', '沙漠守卫_走路左_4', '沙漠守卫_走路左_5', '沙漠守卫_走路左_6', '沙漠守卫_走路左_7', '沙漠守卫_走路左_8']
guard_move_right = ['沙漠守卫_走路右_0', '沙漠守卫_走路右_1', '沙漠守卫_走路右_2', '沙漠守卫_走路右_3', '沙漠守卫_走路右_4', '沙漠守卫_走路右_5', '沙漠守卫_走路右_6', '沙漠守卫_走路右_7', '沙漠守卫_走路右_8']

fail = Actor('闯关失败')
fail.x = 150
fail.y = 100

success = Actor('闯关成功')
success.x = 150
success.y = 100

def draw():
    global flag
    screen.clear()
    screen.blit('沙漠地图', pos=[0, 0])
    wulahu.draw()
    guard.draw()
    if flag == 1:
        fail.draw()
    if flag == 2:
        success.draw()

def update():
    global flag
    global step
    global time
    time += 1
    if flag == 0:
        if wulahu.image != '仙人掌':
            if wulahu.x < guard.x:
                guard.image = guard_move_left[step % 9]
                if time % 2 == 0:
                    guard.x -= 1
            else:
                guard.image = guard_move_right[step % 9]
                if time % 2 == 0:
                    guard.x += 1
            if guard.colliderect(wulahu):
                flag = 1
            if time % 10 == 0:
                step += 1
        else:
            step = 0
            time = 0
        if wulahu.x > 250:
            flag = 2

def on_key_down():
    wulahu.x += 20

def on_mouse_down():
    wulahu.image='仙人掌'


pgzrun.go()
