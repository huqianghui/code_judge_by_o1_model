data = {'机器学习核晶': '反转乾坤', '大数据核晶': '数据回溯', '人工智能伦理核晶': '裁决', '神经网络核晶': '零秒识别', '马文明斯基核晶': '智能创造'}
while True:
    cmd = input()
    if cmd == 'q':
        print('退出')
        break
    elif cmd == 's':
        name = input()
        print(data[name])
    else:
        print('指令无效')