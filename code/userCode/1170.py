def year(y):
    if y % 100 != 0 and y % 4 == 0:
        return '闰年'
    elif y % 400 == 0:
        return '闰年'
    else:
        return '平年'
a=year(966)
print(a)
b=year(1092)
print(b)
c=year(1900)
print(c)