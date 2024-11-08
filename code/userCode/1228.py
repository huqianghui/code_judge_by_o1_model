import pgzrun
import pygame
from PIL import Image
import numpy as np
import joblib

model = joblib.load('手写数字.pkl')
WIDTH = 800
HEIGHT = 540

notice = Actor('提醒', (660, 50))
recog = Actor('识别', (660, 360))
clean = Actor('清除', (660, 460))

result = ''


def draw():
    screen.draw.line((20, 20), (520, 20), 'brown')
    screen.draw.line((520, 20), (520, 520), 'brown')
    screen.draw.line((520, 520), (20, 520), 'brown')
    screen.draw.line((20, 520), (20, 20), 'brown')

    clean.draw()
    recog.draw()
    notice.draw()
    screen.draw.text(str(result), (600, 100), fontsize=300, color='brown')


def on_mouse_move(pos, buttons):
    if mouse.LEFT in buttons:
        screen.draw.filled_circle(pos, 20, 'white')


def on_mouse_down(pos):
    global result
    if recog.collidepoint(pos):
        pygame.image.save(screen.surface, '截图.png')
        img = Image.open('截图.png').convert('L')
        new = img.crop((20, 20, 520, 520))
        img = new.resize((28, 28))
        img_num = np.array(img)
        img_num = img_num.reshape(1, 784)
        pre = model.predict(img_num)
        result = pre[0]


    # ===========在下面编写代码===========
    # 清除按钮被点击时, 清空屏幕
    if clean.collidepoint(pos):
        screen.clear()





        print('先手写数字, 再点击清除按钮才能过关')


pgzrun.go()
