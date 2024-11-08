for i in range(3):
    for j in range(3):
        if j <= i:
            print(i,j)
            print('paint')
            
for k in range(3,6):
    for l in range(3):
        if k + l <= 5:
            print(k,l)
            print('paint')