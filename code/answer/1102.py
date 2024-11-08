for i in range(41, 70):
    # n1,n2分别代表当前编号的个位数字和十位数字
    n1 = i % 10
    n2 = i // 10
    if n1 + n2 == 12:
        print(i)