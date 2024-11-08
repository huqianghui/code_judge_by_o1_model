land = ['AA', 'BB', 'CC', 'DD', 'EE', 'FF']
sea = ['TAC', 'CCB', 'QQE', 'TNJ', 'AUG', 'ZYL']
for i in land:
    print('shoot' + i)
for j in sea:
    if j[0] == j[1]:
       print('pick' + j)
    else:
        print('weed' + j)
