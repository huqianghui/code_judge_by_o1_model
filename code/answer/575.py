def detect(c, r):
    if c == r:
        return 1
    elif c < 3 and r == 4:
        return 2
    else:
        return 0


for i in range(16):
    column = input()
    column = int(column)
    row = input()
    row = int(row)
    n = detect(column, row)
    print(n)