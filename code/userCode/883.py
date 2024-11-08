#输入三个字母, 输出这三个字母能组成的所有字符串
l=input().split()
for a in l:
    for b in l:
        for c in l:
            n=a+b+c
            if n[0]!=n[1] and n[0]!=n[2] and n[1]!=n[2]:
                print(n)