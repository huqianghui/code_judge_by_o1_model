for i in range(4):
    a=input()
    a=a.split('!')
    if len(a)==4:
        a=a[:2]
    elif len(a)==5:
        a=a[:3]
    else:
        a=a[1:]
    print(a)