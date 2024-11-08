import pgzrun
import pygame
from PIL import Image

WIDTH = 440
HEIGHT = 550

clean = Actor('清除', (120, 505))
save = Actor('保存', (320, 505))
notice = Actor('提醒', (180, 30))

number = 0


def draw():
    clean.draw()
    save.draw()
    notice.draw()
    screen.draw.line((20, 60), (420, 60), 'brown')
    screen.draw.line((420, 60), (420, 460), 'brown')
    screen.draw.line((420, 460), (20, 460), 'brown')
    screen.draw.line((20, 460), (20, 60), 'brown')
    screen.draw.text(str(number), (280, 10), fontsize=70, color='white')


def on_mouse_down(pos):
    global number
    if clean.collidepoint(pos):
        screen.clear()
    if save.collidepoint(pos):
        pygame.image.save(screen.surface, '截图.png')
        img = Image.open('截图.png')
        img1 = img.crop((20, 60, 420, 460))
        img1.save(str(number) + '.png')
        print('已经采集了手写数字:', number)
        number = number + 1
        if number == 10:
            number = 0
        screen.clear()


def on_mouse_move(pos, buttons):
    if mouse.LEFT in buttons:
        screen.draw.filled_circle(pos, 20, 'white')


pgzrun.go()
