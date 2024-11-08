def detect(c, r):
        if c == 3:
            return 1
        if c == 4:
            return 1
        else:
            return 0    
for i in range(20):
    column = input()
    column = int(column)
    row = input()
    row = int(row)
    n = detect(column, row)
    print(n)