for r in range(1, 4):
    for c in range(1, 5):
        print(r, c)
        if c == 1:
            print('播种')
        elif c == 3:
            print('浇水')
        else:
            print('除虫')