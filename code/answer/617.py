import pgzrun

WIDTH = 900
HEIGHT = 500

flag = 0
time = 0
step = 0

guard = 0
guard_move_left = []
guard_move_right = []
body = 0

wulahu = Actor('大树')
wulahu.y = 407

guard_sand = Actor('沙滩守卫_左')
guard_sand.x = 280
guard_sand.y = 400
guard_sand_left = ['沙滩守卫_走路左_0', '沙滩守卫_走路左_1', '沙滩守卫_走路左_2', '沙滩守卫_走路左_3', '沙滩守卫_走路左_4', '沙滩守卫_走路左_5', '沙滩守卫_走路左_6',
                   '沙滩守卫_走路左_7', '沙滩守卫_走路左_8']
guard_sand_right = ['沙滩守卫_走路右_0', '沙滩守卫_走路右_1', '沙滩守卫_走路右_2', '沙滩守卫_走路右_3', '沙滩守卫_走路右_4', '沙滩守卫_走路右_5', '沙滩守卫_走路右_6',
                    '沙滩守卫_走路右_7', '沙滩守卫_走路右_8']

guard_forest = Actor('森林守卫_左')
guard_forest.x = 580
guard_forest.y = 400
guard_forest_left = ['森林守卫_走路左_0', '森林守卫_走路左_1', '森林守卫_走路左_2', '森林守卫_走路左_3', '森林守卫_走路左_4', '森林守卫_走路左_5', '森林守卫_走路左_6',
                    '森林守卫_走路左_7', '森林守卫_走路左_8']
guard_forest_right = ['森林守卫_走路右_0', '森林守卫_走路右_1', '森林守卫_走路右_2', '森林守卫_走路右_3', '森林守卫_走路右_4', '森林守卫_走路右_5', '森林守卫_走路右_6',
                     '森林守卫_走路右_7', '森林守卫_走路右_8']

guard_city = Actor('城市守卫_左')
guard_city.x = 880
guard_city.y = 400
guard_city_left = ['城市守卫_走路左_0', '城市守卫_走路左_1', '城市守卫_走路左_2', '城市守卫_走路左_3', '城市守卫_走路左_4', '城市守卫_走路左_5', '城市守卫_走路左_6',
                    '城市守卫_走路左_7', '城市守卫_走路左_8']
guard_city_right = ['城市守卫_走路右_0', '城市守卫_走路右_1', '城市守卫_走路右_2', '城市守卫_走路右_3', '城市守卫_走路右_4', '城市守卫_走路右_5', '城市守卫_走路右_6',
                     '城市守卫_走路右_7', '城市守卫_走路右_8']

fail = Actor('闯关失败')
fail.x = 450
fail.y = 100

success = Actor('闯关成功')
success.x = 450
success.y = 100

def draw():
    global flag
    screen.clear()
    screen.blit('沙滩-森林-城市', pos=[0, 0])
    wulahu.draw()
    guard_sand.draw()
    guard_forest.draw()
    guard_city.draw()
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
        guard = guard_sand
        guard_move_left = guard_sand_left
        guard_move_right = guard_sand_right
        body = '螃蟹'
    elif r == 2:
        guard = guard_forest
        guard_move_left = guard_forest_left
        guard_move_right = guard_forest_right
        body = '大树'
    else:
        guard = guard_city
        guard_move_left = guard_city_left
        guard_move_right = guard_city_right
        body = '垃圾桶'

def update():
    global flag
    global step
    global time
    global guard
    global guard_move_left
    global guard_move_right
    global body
    if wulahu.x > 600:
        guard_init(3)
    elif wulahu.x > 300:
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
        if wulahu.x > 870:
            flag = 2

def on_key_down():
    wulahu.x += 20

def on_mouse_down():
    if wulahu.image == '螃蟹':
        wulahu.image = '大树'
    elif wulahu.image == '大树':
        wulahu.image = '垃圾桶'
    else:
        wulahu.image = '螃蟹'


pgzrun.go()
