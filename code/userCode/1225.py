for i in range(3):
    n = input()
    t = n.split('#')
    if t[0]=='A':
        num=t.count('a')
    if t[0]=='B':
        num=t.count('b')
print(num)
        
        