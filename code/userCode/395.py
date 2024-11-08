a = 0
for i in range(6):
    print('forward')
    m = input()
    m = int(m)
    if m%2==0:
        a+=1
print('forward')
if a>4:
    print('yes')
else:
    print('no')