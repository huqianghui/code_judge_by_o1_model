for i in range(3):
    n = input()
    c = len(n)
    if c == 3:
        s=n[:2]
        print(s)
    else:
        s=n[1:3]
        print(s)