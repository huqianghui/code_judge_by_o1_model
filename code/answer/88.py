for i in range(53, 92):
    n1 = i % 10
    n2 = i // 10
    if n1 + n2 == 13:
        if n1 % n2 == 3:
            print(i)