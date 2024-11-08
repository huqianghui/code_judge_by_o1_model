import pgzrun, random, torch

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
state = None

def draw():
    global bg1, bg2, bird, magma, blocks, score
    bg1.draw()
    bg2.draw()
    bird.draw()
    magma.draw()
    for b in blocks:
        b.draw()
    screen.draw.text(str(score), (20, 10))

# 获取状态
def get_state():
    first_b = blocks[0]
    for b in blocks:
        if (first_b.x < bird.x) or (b.x < first_b.x and b.x > bird.x):
            first_b = b
    state = [bird.y, first_b.x, first_b.y, first_b.type]
    return state

# 返回奖励值最大的动作
def network_predict(state):
    _state = torch.tensor(state, dtype=torch.float32)
    Qs = q_net(_state)
    action = torch.argmax(Qs).item()
    return action

# ---------请在下方编写代码---------
# 加载模型
q_net = torch.load('model.pkl')

def update():
    global score
    state = get_state()
    # 使用模型,得到奖励值最大的动作
    action = network_predict(state)
    # 执行动作
    state1, reward1, done1, score1 = step(action)
    if done1:
        print('游戏结束')
        exit()

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
            reward = -1
            done = True
    if bird.colliderect(magma):
        reward = -1
        done = True

    state = get_state()
    return state, reward, done, score

music.play('bgmusic')
pgzrun.go()