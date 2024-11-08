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
all_button = Actor('all_button.png', (400, 670))

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
    all_button.draw()


def on_mouse_down(pos):
    if nose_button.collidepoint(pos):
        p_nose = random.choice(noses)
        nose.image = 'face/' + p_nose

    if mouth_button.collidepoint(pos):
        p_mouth = random.choice(mouths)
        mouth.image = 'face/' + p_mouth

    if eye_button.collidepoint(pos):
        p_eye = random.choice(eyes)
        left_eye.image = 'face/' + p_eye
        right_eye.image = 'face/' + p_eye
        flip_actor(right_eye)

    if ear_button.collidepoint(pos):
        p_ear = random.choice(ears)
        left_ear.image = 'face/' + p_ear
        right_ear.image = 'face/' + p_ear
        flip_actor(right_ear)

    # "一键变脸"按钮的变量名为all_button
    # 如果鼠标碰到"一键变脸"按钮
    if all_button.collidepoint(pos):
        # 鼻子造型随机变化
        p_nose = random.choice(noses)
        nose.image = 'face/' + p_nose
        # 嘴巴造型随机变化
        p_mouth = random.choice(mouths)
        mouth.image = 'face/' + p_mouth
        # 眼睛造型随机变化
        p_eye = random.choice(eyes)
        left_eye.image = 'face/' + p_eye
        right_eye.image = 'face/' + p_eye
        flip_actor(right_eye)
        # 耳朵造型随机变化
        p_ear = random.choice(ears)
        left_ear.image = 'face/' + p_ear
        right_ear.image = 'face/' + p_ear
        flip_actor(right_ear)


pgzrun.go()
