for r in range(1, 4):
    for c in range(1, 6):
        print(r, c)
        if c == 2 or c == 4:
            print('除虫')
        else:
            print('浇水')