for i in range(4):
    a = input()
    m = a.split('!')
    if len(m) == 5:
        n = m[:3]
    elif len(m) == 4:
        n = m[1:3]
    else:
        n= m[1:]
    print(n)

