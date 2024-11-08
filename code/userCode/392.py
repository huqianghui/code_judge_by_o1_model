import pgzrun
import pygame
from PIL import Image

WIDTH = 800
HEIGHT = 540

notice = Actor('提醒', (660, 50))
recog = Actor('识别', (660, 360))
clean = Actor('清除', (660, 460))


def draw():
    screen.draw.line((20, 20), (520, 20), 'brown')
    screen.draw.line((520, 20), (520, 520), 'brown')
    screen.draw.line((520, 520), (20, 520), 'brown')
    screen.draw.line((20, 520), (20, 20), 'brown')

    clean.draw()
    recog.draw()
    notice.draw()


def on_mouse_move(pos, buttons):
    if mouse.LEFT in buttons:
        screen.draw.filled_circle(pos, 20, 'white')


def on_mouse_down(pos):
    if recog.collidepoint(pos):
        pygame.image.save(screen.surface, '截图.png')
        img = Image.open('截图.png').convert('L')
        # ===========在下面编写代码===========
        # 裁剪出手写区域,并保存为本地文件
        new = img.crop((20,20,520,520))
        new.save('图片.png')




        print('图片已保存')


pgzrun.go()




