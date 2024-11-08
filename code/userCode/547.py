for r in range(1, 5):
    for c in range(1, 4):
        print(r, c)
        # 编写代码,控制小Q打理农场吧.
        if c == 1 or r == 4:
            print('浇水')
        else:
            print('除虫')