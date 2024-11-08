for i in range(10):
    for j in range(10):
        n = 5 * 10000 + i * 1000 + j * 100 + 66
        if n % 57 == 0 and n % 67 == 0:
            print(n)