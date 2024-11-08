n = 0
while n < 4:
    print('forward')
    a=input()
    if a=='bomb' or a=='spider':
        continue
    print('jump')
    n += 1