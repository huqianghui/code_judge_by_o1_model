import pgzrun

WIDTH = 500
HEIGHT = 700

bricks = []
# 修改代码, 创建5个踏板角色并存储到列表bricks中
for b in range(5):
    b = Actor('踏板1')
    bricks.append(b)



def draw():
    screen.blit('背景', [0, 0])
    # 修改代码, 绘制5个踏板角色
    for i in bricks:
        b.draw()


pgzrun.go()