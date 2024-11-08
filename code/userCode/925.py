import pgzrun
import random

HEIGHT = 500
WIDTH = 1000
TITLE = '丛林跑酷'

bg1 = Actor('bg', [500, 250])
bg2 = Actor('bg', [1500, 250])

player = Actor('player_run1', [80, 300])

golds = []
for i in range(2):
    n = random.randint(1, 3)
    g = Actor('gold' + str(n))
    g.x = 800 * (i + 1)
    g.y = random.randint(100, 220)
    golds.append(g)

blocks = []
for i in range(3):
    n = random.randint(1, 6)
    b = Actor('barrier' + str(n))
    b.x = 600 * (i + 1)
    b.y = 340 - b.height / 2
    blocks.append(b)

num = 1
action = '跑'


def draw():
    global num, action
    bg1.draw()
    bg2.draw()

    for b in blocks:
        b.draw()

    for g in golds:
        g.draw()

    if action == '跑':
        player.image = 'player_run' + str(num)
        num = num + 1
        if num > 10:
            num = 1
    elif action == '跳':
        player.image = 'player_jump'

    player.draw()



def update():
    global player, golds, blocks, action

    bg1.x -= 2
    bg2.x -= 2

    if bg1.right < 0:
        bg1.x = 1500
    if bg2.right < 0:
        bg2.x = 1500

    for b in blocks:
        b.x -= 2
        if b.right < 0:
            n = random.randint(1, 6)
            b.image = 'barrier' + str(n)
            b.x = random.randint(1000, 1500)
            b.y = 340 - b.height / 2

    for g in golds:
        g.x -= 2
        if g.right < 0:
            n = random.randint(1, 3)
            g.image = 'gold' + str(n)
            g.x = random.randint(1000, 1500)
            g.y = random.randint(100, 220)

    if action == '跑' or action == '跳':
        # 按住空格键,小酷跳起
        if keyboard.space:
            if player.y > 100:
                player.y -= 8
                # 此时应该是'跳'的状态
                action = '跳'

        else:
            if player.y < 300:
                player.y += 8
                # 此时应该是'跳'的状态
                action = '跳'

            if player.y == 300:
                # 此时应该是'跑'的状态
                action = '跑'








music.play('bg_music')

pgzrun.go()