import pgzrun

WIDTH = 800
HEIGHT = 800

info = ['你是一位雄心勃勃的国王',
        '你的使命是:提升国民的幸福感、\n提升军事实力、维持国家安定统一',
        '大臣们会为你提供各种治国建议,\n你需要对这些建议作出抉择',
        '每一项决策都会影响到\n你自己的声望值和财富值',
        '声望和财富上升,会得到国民拥戴;\n反之,也会引起民众的不满',
        '点击任意位置开始游戏,\n履行你作为国王的使命吧......']

state = 'begin'
n = 0

yes = Actor('同意按钮')
yes.x = 75
yes.y = 550
no = Actor('驳回按钮')
no.x = 725
no.y = 550
king = Actor('国王')
king.x = 430
king.y = 530

score1 = 10
score2 = 10

def draw():
    global n, score1, score2
    if state == 'begin':
        screen.blit('开始背景', (0, 0))
        if n < 6:
            words = info[n]
            screen.draw.text(words, (100, 80), fontname='puhuiti.ttf', fontsize=40, color='black')
    elif state == 'choice':
        screen.blit('决策背景', (0, 0))
        king.draw()
        no.draw()
        yes.draw()

        ques = '要建立军队吗?'
        screen.draw.text(ques, (280, 140), fontname='puhuiti.ttf', fontsize=40, color='black')
        screen.draw.text('声望: ' + str(score1), (150, 20), fontname='puhuiti.ttf', fontsize=45, color='darkviolet')
        # 将财富值显示到窗口中
        screen.draw.text('财富: ' + str(score2), (500, 20), fontname='puhuiti.ttf', fontsize=45, color='brown')


def on_mouse_down(button):
    global n, state
    if button == mouse.LEFT:
        n += 1
        if n == 6:
            state = 'choice'

music.play('king_song')
pgzrun.go()