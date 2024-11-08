'''
scores = [[100, 80, 82, 88...],
        [97, 85, 88, 64...], 
                ...
        [72, 53, 77, 92...]]
'''
count = 0
for x in scores:
    for b in x:
        if b > 90:
            c += 1
print()