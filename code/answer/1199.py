for i in range(3):
    n = input()
    t = n.split('@')
    s = 0
    for i in t:
        a = int(i)
        s += a
    print(s)

# 或
for i in range(3):
    n = input()
    t = n.split('@')
    s = 0
    for i in t:
        s += int(i)
    print(s)   
