for r in range(1, 6):
    for c in range(1, 6):
        print(r, c)
        # 编写代码,控制小Q打理农场吧.
        if r == c or r + c == 6:
            print('采摘')
        else:
            print('浇水')