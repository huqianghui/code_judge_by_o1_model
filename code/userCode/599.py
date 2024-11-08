for i in range(3):
    n = input()
    t = n.split('#')
    if t[0] == 'D':
        num = t.count('d')
    if t[0] == 'E':
        num = t.count('e')
    print(num)