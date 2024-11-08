x = 7
while x < 15:
    a = input()
    # 获取能量包上的数字
    n = int(a[1])
    # 如果能量包是可充能类型, 打印收集指令, 并增加能量值
    if a[0] == 'Y':
        print('get')
        x += n
# 打印战机加速指令
print('speed')