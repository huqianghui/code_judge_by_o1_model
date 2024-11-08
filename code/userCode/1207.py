import json
import os
import requests
import pygame
import pgzrun
import random


u = 'https://www.hetao101.com/api/classification'
img_list = os.listdir('images/face')

noses = []
eyes = []
ears = []
mouths = []

for i in img_list:
    path = 'face/' + i
    img = open_deal_image(path)
    response = requests.post(url=u, data=img)
    r = json.loads(response)
    results = r['results']
    s = 0
    n = ''
    for j in results:
        if j['score'] > s:
            s = j['score']
            n = j['name']

    if n == '鼻子':
        noses.append(i)
    elif n == '嘴巴':
        mouths.append(i)
    elif n == '眼睛':
        eyes.append(i)
    elif n == '耳朵':
        ears.append(i)


print('鼻子列表noses:', noses)
print('嘴巴列表mouths:', mouths)
print('眼睛列表eyes:', eyes)
print('耳朵列表ears:', ears)


WIDTH = 800
HEIGHT = 800


def flip_actor(actor):
    actor._surf = pygame.transform.flip(actor._surf, True, False)


nose = Actor('face/1.png', (300, 400))
mouth = Actor('face/31.png', (300, 500))

left_eye = Actor('face/11.png', (200, 350))
right_eye = Actor('face/11.png', (400, 350))
flip_actor(right_eye)

left_ear = Actor('face/14.png', (80, 370))
right_ear = Actor('face/14.png', (520, 370))
flip_actor(right_ear)

eye_button = Actor('eye_button.png', (700, 150))
ear_button = Actor('ear_button.png', (700, 250))
nose_button = Actor('nose_button.png', (700, 350))
mouth_button = Actor('mouth_button.png', (700, 450))


def draw():
    screen.blit('头像背景', (0, 0))
    nose.draw()
    mouth.draw()
    left_eye.draw()
    right_eye.draw()
    left_ear.draw()
    right_ear.draw()

    eye_button.draw()
    ear_button.draw()
    nose_button.draw()
    mouth_button.draw()


def on_mouse_down(pos):
    if nose_button.collidepoint(pos):
        p_nose = random.choice(noses)
        nose.image = 'face/' + p_nose

    # 检测鼠标是否碰到嘴巴按钮
    if mouth_button.collidepoint(pos):
        # 从mouths列表中随机选择一个元素
        p_mouth = random.choice(mouths)
        # 修改嘴巴造型
        mouth.image = 'face/' + p_mouth


pgzrun.go()
