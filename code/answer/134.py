for r in range(1, 5):
    for c in range(1, 6):
        print(r, c)
        if r == 2:
            print('除虫')
        elif r == 4:
            print('播种')
        else:
            print('浇水')