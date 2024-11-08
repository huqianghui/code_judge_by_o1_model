import pgzrun

WIDTH = 600
HEIGHT = 500

flag = 0
time = 0
step = 0

guard = 0
guard_move_left = []
guard_move_right = []
body = 0

wulahu = Actor('螃蟹')
wulahu.y = 407

guard_south = Actor('南极守卫_左')
guard_south.x = 280
guard_south.y = 400
guard_south_left = ['南极守卫_走路左_0', '南极守卫_走路左_1', '南极守卫_走路左_2', '南极守卫_走路左_3', '南极守卫_走路左_4', '南极守卫_走路左_5', '南极守卫_走路左_6', '南极守卫_走路左_7', '南极守卫_走路左_8']
guard_south_right = ['南极守卫_走路右_0', '南极守卫_走路右_1', '南极守卫_走路右_2', '南极守卫_走路右_3', '南极守卫_走路右_4', '南极守卫_走路右_5', '南极守卫_走路右_6', '南极守卫_走路右_7', '南极守卫_走路右_8']

guard_sand = Actor('沙滩守卫_左')
guard_sand.x = 580
guard_sand.y = 400
guard_sand_left = ['沙滩守卫_走路左_0', '沙滩守卫_走路左_1', '沙滩守卫_走路左_2', '沙滩守卫_走路左_3', '沙滩守卫_走路左_4', '沙滩守卫_走路左_5', '沙滩守卫_走路左_6', '沙滩守卫_走路左_7', '沙滩守卫_走路左_8']
guard_sand_right = ['沙滩守卫_走路右_0', '沙滩守卫_走路右_1', '沙滩守卫_走路右_2', '沙滩守卫_走路右_3', '沙滩守卫_走路右_4', '沙滩守卫_走路右_5', '沙滩守卫_走路右_6', '沙滩守卫_走路右_7', '沙滩守卫_走路右_8']

fail = Actor('闯关失败')
fail.x = 300
fail.y = 100

success = Actor('闯关成功')
success.x = 300
success.y = 100

def draw():
    global flag
    screen.clear()
    screen.blit('南极-沙滩', pos=[0, 0])
    wulahu.draw()
    guard_south.draw()
    guard_sand.draw()
    if flag == 1:
        fail.draw()
    if flag == 2:
        success.draw()

def guard_init(r):
    global flag
    global guard
    global guard_move_left
    global guard_move_right
    global body
    if r == 1:
        guard = guard_south
        guard_move_left = guard_south_left
        guard_move_right = guard_south_right
        body = '企鹅'
    else:
        guard = guard_sand
        guard_move_left = guard_sand_left
        guard_move_right = guard_sand_right
        body = '螃蟹'

def update():
    global flag
    global step
    global time
    global guard
    global guard_move_left
    global guard_move_right
    global body
    if wulahu.x > 300:
        guard_init(2)
    else:
        guard_init(1)
    time += 1
    if flag == 0:
        if wulahu.image != body:
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
        if wulahu.x > 570:
            flag = 2

def on_key_down():
    wulahu.x += 20

def on_mouse_down():
    if wulahu.image=='螃蟹':
        wulahu.image='企鹅'    
    else:
        wulahu.image='螃蟹'    
           


    


pgzrun.go()