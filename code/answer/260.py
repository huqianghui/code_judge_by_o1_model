for i in range(4):
    a = input()
    m = a.split('!')
    if len(m) == 4:
        n = m[:2]
    elif len(m) == 5:
        n = m[:3]
    else:
        n= m[1:]
    print(n)

