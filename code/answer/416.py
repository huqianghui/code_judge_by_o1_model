for i in range(3):
    n = input()
    t = n.split('@')
    s = 0
    for i in t:
        a = int(i)
        if a < 100:
            s += a
    print(s)
