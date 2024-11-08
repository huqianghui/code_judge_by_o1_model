a = 0
for i in range(11):
    print('forward')
    m=input()   
    m=int(m)
    if m%2==1:
        a+=1
print('forward')
if a < 3:
    print('yes')
else:
    print('no')
