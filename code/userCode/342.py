x = 5
while x < 10:
    # 接收能量包信息
    a = input()
    # 判断能量包是否可充能
    if a == 'Y1':
        # 打印收集指令
        print('get')
        # 给能量值x加1
        x+=1
print('speed')