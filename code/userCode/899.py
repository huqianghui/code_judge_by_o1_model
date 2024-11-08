sizes = input()
o = 0
for i in sizes:
    n = int(i)
    if n > 3:
        o += 1
        print('A')
    else:
        print('B')
print(o)