d = input()
for i in range(len(d) - 1):
    if d[i] == 'T' and d[i + 1] == 'G':
        print(i)
