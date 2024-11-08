
for i in range(10):
    for j in range(10):
        ans = 5 * 10000 + i * 1000 + j * 100 + 66
        if ans % 57 == 0 and ans % 67 == 0:
            print( ans)