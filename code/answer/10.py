for r in range(1, 6):
    for c in range(1, 6):
        print(r, c)
        if r == c:
            print('采摘')
        else:
            print('浇水')