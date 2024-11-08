import pgzrun

WIDTH = 800
HEIGHT = 800

info = ['你是一位雄心勃勃的国王',
        '你的使命是:提升国民的幸福感、提升军事实力、维持国家安定统一',
        '大臣们会为你提供各种治国建议, 你需要对这些建议作出抉择',
        '每一项决策都会影响到你自己的声望值和财富值',
        '声望和财富上升, 会得到国民拥戴;反之, 也会引起民众的不满',
        '点击任意位置开始游戏, 履行你作为国王的使命吧......']

n = 0

def draw():
    global n
    screen.blit('开始背景', (0, 0))
    # 当n的值不超过info的最大索引时,才进行绘制
    if n > 5:
        # 根据鼠标点击次数,绘制中对应的句子
        words = info[n]
        screen.draw.text(words, (100, 80), fontname='puhuiti.ttf', fontsize=40, color='black')


def on_mouse_down():
    # 声明全局变量n用于记录鼠标点击次数
    global n
    # 每点击一次鼠标,n增加1
    


music.play_once('king_song')
pgzrun.go()