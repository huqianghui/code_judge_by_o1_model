import pgzrun

WIDTH = 500
HEIGHT = 700

player = Actor('小核桃')
player.x = 250
player.y = 650


def draw():
    screen.blit('星球', [0, 0])
    player.draw()

# 定义on_key_down()函数, 用方向键控制小核桃上下左右移动
'''
按键名称: 
左方向键  keys.LEFT
右方向键  keys.RIGHT
上方向键  keys.UP
下方向键  keys.DOWN
'''

def on_key_down(key):
    if key == keys.LEFT:
        player.x -= 20
    if key == keys.RIGHT:
        player.x += 20
    # 在这里编写代码
    if key == keys.UP:
        player.y -= 20
    if key == keys.DOWN:
        player.y += 20

pgzrun.go()









