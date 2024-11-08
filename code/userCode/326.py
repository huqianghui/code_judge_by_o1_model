a=int(input())
if a%3==0:
    if a%4==0:
        a=a//12
    else:
        a=a%12
else:
    a+=3
print(a)