numbers = input().split()
# 大嘴花的重量有整数, 也有小数
s=0
for i in numbers:
    s+=float(i)
print(s)