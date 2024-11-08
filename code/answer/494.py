n = 0
while n < 4:
    print('forward')
    name = input()
    if name == 'bomb' or name == 'spider':
        continue
    print('jump')
    n += 1
