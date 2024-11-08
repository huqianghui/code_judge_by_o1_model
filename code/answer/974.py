for i in range(12):
    print('next')
    a = input()
    a = int(a)
    if a > 8:
        print('red')
    elif a % 3 == 0:
        print('yellow')
    elif a % 3 == 2:
        print('green')