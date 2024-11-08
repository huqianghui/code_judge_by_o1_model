n=input()
for x in range(len(n)):
    if n[x]=='T' and n[x+1]=='G':
        print(x)