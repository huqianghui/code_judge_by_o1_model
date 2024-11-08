def cal_reward(state):
    reward = 0
    if state == 17:
        reward += 10
    elif state in [13,14,15,16]:
        reward -= 1
    return reward


def reinforcementLearning():
    global state
    createQtable() # 创建q表
    for i in range(20): # 训练次数
        reset() # 配置初始环境
        end = False
        while not end:
            last_state = state
            # 1 选择动作
            current_action = choose_action(state)
            # 2 执行动作
            step(current_action)
            # 3 计算奖励
            reward = cal_reward(state)
            # 4 更新q表
            updateTable(reward, last_state, current_action)
            end = checkEnding()