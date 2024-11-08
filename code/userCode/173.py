import pgzrun
import os

WIDTH = 400
HEIGHT = 600

# 爬取的歌曲名称
names = []
songs = os.listdir('music')
for s in songs:
    names.append(s.split('.')[0])

# 列表索引
now = 0
cd = Actor(names[now], (200, 200))
button = Actor('播放', (200, 400))
button_pre = Actor('上一首', (100, 400))
button_next = Actor('下一首', (300, 400))
buttons = [button, button_pre, button_next]


def draw():
    global now
    screen.blit('背景', (0, 0))
    for button in buttons:
        button.draw()
    cd.draw()
    # 绘制歌曲名称
    screen.draw.text(names[now], (25, 30), color='white', fontsize=35, fontname='方正黑体简体.ttf')


def on_mouse_down(pos):
    global now
    if button.collidepoint(pos):
        if button.image == '播放':
            music.play(names[now])
            button.image = '停止'
        else:
            music.stop()
            button.image = '播放'
    # 播放下一首
    if button_next.collidepoint(pos):
        if now == len(names) - 1:
            now = 0
        else:
            now += 1
        music.play(names[now])
        cd.image = names[now]
        button.image = '停止'
    # 播放上一首
    # 判断鼠标是否点击了上一首
    if button_pre.collidepoint(pos):
        # 改变索引now的值
        # 注意now不能无限减小,等于0时要赋值为索引最大值
       if now ==0:
           new=len(names)-1
       else:
           now-=1


        music.play(names[now])
        cd.image = names[now]
        button.image = '停止'


pgzrun.go()
