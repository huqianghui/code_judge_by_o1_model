def move(r):
    if r<2:
        return('down')
    elif r>2:
        return('up')
    else:
        return('left')

while True:
    column = input()
    column = int(column)
    row = input()
    row = int(row)
    if column == 1 and row == 2:
        break
    order = move(row)
    print(order)
