s = 9
while s > 5:
    print('get')
    a = input()
    if a == 'green':
        print('throw')
        s -= 1
    if a == 'red':
        print('throw')
        s -= 2
print('start')