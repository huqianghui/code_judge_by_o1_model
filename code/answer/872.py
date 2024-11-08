for i in range(2):
    n = input()
    t = n.split('#')
    x = t.count('e')
    y = t.count('ee')
    if x > y:
        print(x)
    else:
        print(y)
