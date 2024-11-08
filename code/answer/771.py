n = int(input())
x = 0
while x < n:
    m = int(input())
    if m >= 200:
        print('L-camera')
    if m < 200 and m >= 100:
        print('M-camera')
    x += 1
print('go')
