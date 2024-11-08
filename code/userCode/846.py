import pgzrun

WIDTH = 500
HEIGHT = 700

player = Actor('小核桃')
player.x = 250
player.y = 650


def draw():
    screen.blit('星球', [0, 0])
    player.draw()

# 定义on_key_down()函数: 按下空格键, 创建子弹角色, 并让子弹位于小核桃的位置
# 按键名称: 空格键 keys.SPACE
def on_key_down(key):
    if key == keys.LEFT:
        player.x -= 20
    if key == keys.RIGHT:
        player.x += 20
    if key == keys.UP:
        player.y -= 20
    if key == keys.DOWN:
        player.y += 20
    # 在这里编写代码
    if key==keys.SPACE:
        weapon=Actor("子弹")
        weapon.x=player.x
        weapon.y=player.y
pgzrun.go()