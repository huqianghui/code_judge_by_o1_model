# 在某个状态下, 选择动作
def choose_action(state):
    # 非贪心模式, 随机选择一个动作
    if random.random() > greedy:
        action = random.randint(0, 8)
    # 贪心模式, 选择奖励最大的动作
    else:
        # 获取这个状态下的所有动作的奖励值列表
        state_actions = STATE_L[state]

        # ===找出列表中的最大奖励值===
        max_reward = max(action)
        # ===找出最大奖励值对应的动作===
        action = action.index()

    # 返回动作
    return action