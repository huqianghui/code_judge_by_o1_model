import pgzrun

# 设置窗口的宽和高
WIDTH = 800
HEIGHT = 800

def draw():
    # 绘制背景
    screen.blit('开始背景', (0, 0))

music.play_once('king_song')
pgzrun.go()