def step(action):
    global state
    if action == 'left':
        if state % 6 != 0:
            state -= 1
    elif action == 'right':
        if state % 6 != 5:
            state += 1
    # 编写代码,实现角色向上和向下移动
    elif action == 'up':
        if state > 5:
            state -= 6
    elif action == 'down':
        if state < 12:
            state += 6 
    # 如果角色掉入悬崖,需返回出发点
    if state in [13,14,15,16]:
        state = 12
    if state == 17:
        print('吃到金币了')