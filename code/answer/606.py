t = 0
while t < 3:
    color = input()
    if t == 0 and color == 'green':
        print('shoot')
        t += 1
    elif t == 1 and color == 'blue':
        print('shoot')
        t += 1
    elif t == 2 and color == 'red':
        print('shoot')
        t += 1
    else:
        print('change')