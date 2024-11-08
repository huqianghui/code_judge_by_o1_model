for i in range(3):
    n = input()
    w = len(n)
    if w==5:
        s = n[3:]
    else:
        s = n[3:5]
print(s)