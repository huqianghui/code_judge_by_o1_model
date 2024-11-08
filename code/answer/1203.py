a = 0
b = 0
for i in range(10):
    print('forward')
    m = input()
    if m == '2':
        a += 1
    else:
        b += 1
print('forward')
if a > b:
    print('number2')
else:
    print('number3')