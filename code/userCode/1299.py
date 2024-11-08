import pgzrun

WIDTH = 800
HEIGHT = 800

def draw():
    screen.blit('开始背景', (0, 0))
    words = '你是一位雄心勃勃的国王'
    # 设置字体、字号和颜色
    screen.draw.text(words, (120, 150), )      
    screen.draw.text(words, (120, 150),fontname='puhuiti.ttf',
    fontsize=40,color='black')
music.play_once('king_song')
pgzrun.go()