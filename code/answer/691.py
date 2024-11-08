hp = 100
while hp > 0:
    a = input()
    print('shoot')
    if a == 'yellow':
        hp -= 10
    if a == 'red':
        hp -= 20