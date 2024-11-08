import pgzrun

WIDTH = 800
HEIGHT = 800

info = ['你是一位雄心勃勃的国王',
        '你的使命是:提升国民的幸福感、\n提升军事实力、维持国家安定统一',
        '大臣们会为你提供各种治国建议,\n你需要对这些建议作出抉择',
        '每一项决策都会影响到\n你自己的声望值和财富值',
        '声望和财富上升,会得到国民拥戴;\n反之,也会引起民众的不满',
        '点击任意位置开始游戏,\n履行你作为国王的使命吧......'
        ]

question = [['要建立军队吗?', '大臣建议攻打邻国,\n以获得更多土地', '邻国攻打,国家灭亡', 1, 100],
            ['要攻打邻国吗?', '战争胜利,获得了大片土地,\n但战争也消耗了大量财产,\n国库亏空', '本国没有发动战争,\n但也十分忌惮邻国的军队', 2, 3],
            ['要增加民众税收\n填补国库的亏空吗?', '民众被税收压得怨声载道,\n为了平民愤,\n大臣提出一个办法', '大力发展农业来填补国库亏空,\n经济复苏',4, 5],
            ['要花费大量金钱\n购买武器吗?', '花费了大量金钱,国库亏空',  '邻国突然发起战争,\n由于缺乏武器,战败亡国', 2, 100],
            ['要将愤怒的民众\n发配边疆吗?', '军队被大量扩充后,\n其他国家结盟发起进攻\n连年征战,民不聊生......',  '愤怒的民众发动起义,\n将你推下王位,取而代之......', 100, 100],
            ['要将多余的财产\n用来推广教育吗?','民众的素质提升,文学、经济等\n都发展良好,国家繁荣昌盛', '民众的素质低下,\n经常因为一些小事发生冲突,\n好不容易复苏的经济也变为泡沫,\n人民困苦不堪......', 100, 100]
            ]

qi = 0
ci = 0

state = 'begin'
n = 0

king = Actor('国王')
king.x = 430
king.y = 530
yes = Actor('同意按钮')
yes.x = 75
yes.y = 550
no = Actor('驳回按钮')
no.x = 725
no.y = 550

score1 = 10
score2 = 10

def draw():
    global n, state, score1, score2
    if state == 'begin':
        screen.blit('开始背景', (0, 0))
        words = info[n]
        screen.draw.text(words,
            (100, 80),
            fontname='puhuiti.ttf',
            fontsize=40,
            color='black')
    elif state == 'choice':
        screen.blit('决策背景', (0, 0))
        king.draw()
        no.draw()
        yes.draw()
        screen.draw.text('声望: ' + str(score1),
            (150, 20),
            fontname='puhuiti.ttf',
            fontsize=45,
            color='darkviolet')
        screen.draw.text('财富: ' + str(score2),
            (500, 20),
            fontname='puhuiti.ttf',
            fontsize=45,
            color='brown')
        screen.draw.text(question[qi][0],
            (280, 140),
            fontname='puhuiti.ttf',
            fontsize=40,
            color='royalblue2')
    elif state == 'show':
        screen.blit('展示背景', (0, 0))
        screen.draw.text(question[qi][ci],
            (100, 150),
            fontname='puhuiti.ttf',
            fontsize=40,
            color='black')

def on_mouse_down(button, pos):
    global n, state, qi, ci
    if button == mouse.LEFT:
        if state == 'begin':
            n += 1
            if n == 6:
                state = 'choice'
                qi = 0
        elif state == 'choice':
            if yes.collidepoint(pos):
                state = 'show'
                ci = 1
            elif no.collidepoint(pos):
                state = 'show'
                ci = 2
        elif state == 'show':
            if ci == 1:
                qi = question[qi][3]
            elif ci == 2:
                qi = question[qi][4]
            #===========================
            #在下方编写代码,当故事走到结局,
            #把state设为end
            #===========================
            if qi < 100:
                state = 'choice'
            else:
                state = 'end'
            
            



music.play('king_song')
pgzrun.go()







