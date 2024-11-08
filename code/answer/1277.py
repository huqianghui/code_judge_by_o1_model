for i in range(4):
    n = input()
    t = n.split('#')
    if t[0] == 'A':
        x = t.count('a')
        print(x)
    if t[0] == 'E':
        x = t.count('e')
        y = t.count('ee')
        if x > y:
            print(x)
        else:
            print(y)
