# 第一部分:游戏
import pgzrun, random

WIDTH = 1000
HEIGHT = 500

def init_game():
    global score, names, num, bg1, bg2, bird, magma, b1, b2, b3, blocks
    score = 0
    names = ['藤蔓', '枝干', '尖刺']
    num = [100, 75, 400]
    bg1 = Actor('背景图1')
    bg1.x = 500
    bg1.y = 250
    bg2 = Actor('背景图2')
    bg2.x = bg1.x + 1000
    bg2.y = 250
    magma = Actor('岩浆1')
    magma.x = 500
    magma.y = 480
    bird = Actor('月月鸟1')
    bird.x = 200
    bird.y = 100
    b1 = Actor('藤蔓')
    b1.x = 1000
    b1.y = 100
    b1.type = names.index(b1.image)
    b2 = Actor('枝干')
    b2.x = 1600
    b2.y = 75
    b2.type = names.index(b2.image)
    b3 = Actor('尖刺')
    b3.x = 2100
    b3.y = 400
    b3.type = names.index(b3.image)
    blocks = [b1, b2, b3]

init_game()
FPS = 0
subtract = Actor('减')
subtract.x = 50
subtract.y = 420
plus = Actor('加')
plus.x = 150
plus.y = 420

def draw():
    global bg1, bg2, bird, magma, blocks, score
    bg1.draw()
    bg2.draw()
    bird.draw()
    magma.draw()
    for b in blocks:
        b.draw()
    subtract.draw()
    plus.draw()
    screen.draw.text(str(FPS), (90, 410))
    screen.draw.text(str(score), (20, 10))

def on_mouse_down(pos):
    global FPS
    if subtract.collidepoint(pos):
        if FPS > 0:
            FPS -= 1
    if plus.collidepoint(pos):
        FPS += 1

def get_state():
    first_b = blocks[0]
    for b in blocks:
        if (first_b.x < bird.x) or (b.x < first_b.x and b.x > bird.x):
            first_b = b
    state = [bird.y, first_b.x, first_b.y, first_b.type]
    return state

def update():
    pass

def reset():
    init_game()
    state = get_state()
    return state

def step(action):
    global score
    state = None
    reward = 0
    done = False
    if action == 1:
        if bird.y > 35:
            bird.y -= 5
    else:
        if bird.y < 465:
            bird.y += 5
    if bird.image == '月月鸟1':
        bird.image = '月月鸟2'
    else:
        bird.image = '月月鸟1'
    if magma.image == '岩浆1':
        magma.image = '岩浆2'
    else:
        magma.image = '岩浆1'
    bg1.x -= 7
    bg2.x -= 7
    if bg1.x < -500:
        bg1.x = bg2.x + 1000
    if bg2.x < -500:
        bg2.x = bg1.x + 1000
    for b in blocks:
        b.x -= 5
        if b.x < -30:
            b.x = 1500
            n = random.randint(0, 2)
            b.type = n
            b.y = num[n]
            b.image = names[n]
            score += 1
            reward = 1
        if bird.colliderect(b):
            print('碰到障碍物')
            reward = -1
            done = True
    if bird.colliderect(magma):
        print('碰到岩浆')
        reward = -1
        done = True

    state = get_state()
    return state, reward, done, score

# 第二部分:模型
import random, time, sys
import torch

# 构造神经网络
def create_net():
    q_net = torch.nn.Sequential(
        torch.nn.Linear(4, 256),
        torch.nn.ReLU(),
        torch.nn.Linear(256, 128),
        torch.nn.ReLU(),
        torch.nn.Linear(128, 2)
    )
    return q_net

# 强化学习
def main_loop():
    global q_net, exp_pool
    q_net = create_net()
    # 定义数据池,用来存储数据,以供神经网络训练
    exp_pool = []

    while True:
        # 初始化游戏
        state = reset()
        while True:
            # 控制刷新频率,可在界面左下角调节
            time.sleep(FPS/1000)
            # ---------请在下方编写代码---------
            # 随机选择一个动作
            action = random.randint(0, 1)
            # 执行动作
            next_state, reward, done, score1 = step(action)
            # 将本次的状态、奖励、动作,新状态、是否结束存到数据池里
            exp_pool.append([state, reward, action, next_state, done])
            # 保存最新的状态
            state = next_state
            # 判断本轮游戏是否结束
            if done:
                break


# 第三部分:启动游戏
import _thread

def one_thread(threadName, delay):
    time.sleep(0.5)
    main_loop()
_thread.start_new_thread(one_thread, ('Thread-1', 1))

music.play('bgmusic')
pgzrun.go()