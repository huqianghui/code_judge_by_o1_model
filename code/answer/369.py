sizes = input()
a = 0    # 存储A级果的数量
b = 0    # 存储B级果的数量
c = 0    # 存储C级果的数量
for x in sizes:
    n = int(x)
    if n > 3:
        a += 1
    elif n == 1:
        c += 1
    else:
        b += 1
print(a, b, c)