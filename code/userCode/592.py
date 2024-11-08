import pgzrun

WIDTH = 800
HEIGHT = 800

info = ['你是一位雄心勃勃的国王',
        '你的使命是:提升国民的幸福感、\n提升军事实力、维持国家安定统一',
        '大臣们会为你提供各种治国建议, \n你需要对这些建议作出抉择',
        '每一项决策都会影响到\n你自己的声望值和财富值',
        '声望和财富上升,会得到国民拥戴;\n反之,也会引起民众的不满',
        '点击任意位置开始游戏, \n履行你作为国王的使命吧......']

n = 0

def draw():
    global n
    screen.blit('开始背景', (0, 0))
    if n < 6:
        words = info[n]
        screen.draw.text(words, (100, 80), fontname='puhuiti.ttf', fontsize=40, color='black')


# 填写函数on_mouse_down的参数,用于判断鼠标操作
def on_mouse_down(button):
    global n
    # 判断按下的是否是鼠标左键
    if button == mouse.LEFT:
        n += 1


music.play_once('king_song')
pgzrun.go()