for r in range(1, 5):
    for c in range(1, 4):
        print(r, c)
        if r == 4 or c == 1:
            print('浇水')
        else:
            print('除虫')