rule = {1: '石头', 2: '剪刀', 3: '布'}
n = input('请输入回合数:')
n = int(n)
r = 
while r < n:
    p=input('请输入手势编号:')
    p=int(p)
    print('玩家选择',rule[p])
    r += 1