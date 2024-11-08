def move(c, r):
    if r < 3:
        return 'down'
    elif r > 3:
        return 'up'
    else:
        if c < 4:
            return 'right'
        if c > 4:
            return 'left'

while True:
    column = input()
    column = int(column)
    row = input()
    row = int(row)
    if column == 4 and row == 3:
        break
    order = move(column, row)
    print(order)
