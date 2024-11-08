land = ['AA', 'BB', 'CC', 'DD', 'EE', 'FF']
sea = ['TAC', 'HJK', 'SER', 'DNN', 'ZCC', 'BYL']
for i in land:
    print('shoot' + i)
for j in sea:
    if j[1]==j[2]:
        print('pick'+j)
    else:
        print('weed' + j)