x = 9
while x > 5:
    print('get')    
    a = input()
    if a == 'green':
        print('throw')
        x -= 1
    if a == 'red':
        print('throw')
        x -= 2
print('start')