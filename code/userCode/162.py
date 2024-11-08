import random
rule = {1: '石头', 2: '剪刀', 3: '布'}
n = input('请输入回合数:')
n = int(n)
r = 0
score_p = 0
score_c = 0
while r < n:    
    p = input('请输入手势编号:')
    p = int(p)
    if p not in rule.keys():
        print('编号错误,请重新输入')
        continue
    print('玩家选择:', rule[p])
    c = random.randint(1, 3)
    print('电脑选择:', rule[c])
    if (p == 1 and c == 2) or (p == 2 and c == 3) or (p == 3 and c == 1):
        score_p += 1
    elif p == c:
        score_p += 1
        score_c += 1
    else:
        score_c += 1
    r += 1
print(score_p)
print(score_c)