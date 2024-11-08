import pygame
import pgzrun


# 设置人像
people = Actor('响应')
# 设置背景
bg = Actor('背景')


def draw():
    screen.clear()
    bg.draw()
    people.draw()


def update():
    if keyboard.s:
        pygame.image.save(screen.surface, 'images/合成结果.png')
        exit()
    # =====方向键控制people角色向对应方向移动=====
    if keyboard.left:
        people.x -= 1
    if keyboard.right:
        people.x += 1
    if keyboard.up:
        people.y -= 1
    if keyboard.down:
        people.y += 1
TITLE = '图片合成'
WIDTH, HEIGHT = bg._surf.get_size()
pgzrun.go()
