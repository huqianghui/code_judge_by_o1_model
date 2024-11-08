for i in range(4):
    a=input()
    b=a.split('!')
    if len(b)==5:
        c=b[:3]
    elif len(b)==4:
        c=b[1:3]
    else:
        c=b[1:]
    print(c)
        