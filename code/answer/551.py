greedy = 0.9
def choose_action(state):
    global greedy
    if q_table[state]['left'] == q_table[state]['right'] == q_table[state]['up'] == q_table[state]['down'] or random.random() > greedy:
        current_action = random.choice(ACTION)
    else:
        current_action = findMaxDict(q_table[state])
    return current_action


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