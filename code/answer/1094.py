# 在某个状态下, 选择动作
def choose_action(state):
    if random.random() > greedy:
        action = random.randint(0, 8)
    # 贪心模式, 选择奖励最大的动作
    else:
        # 获取这个状态下的动作奖励值列表
        state_actions = STATE_L[state]
        # 找出其中的奖励最大值
        max_reward = max(state_actions)

        max_same = []
        # 遍历动作奖励值列表
        for i in range(len(state_actions)):
            # 如果元素的值与最大奖励相同
            if state_actions[i] == max_reward:
                # ==将元素索引加入max_same列表==
                max_same.append(i)
        # ==从max_same列表中随机选取一个动作==
        action = random.choice(max_same)

    return action