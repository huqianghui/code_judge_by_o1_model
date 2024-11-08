def year(y):
    if y % 100 != 0 and y % 4 == 0:
        return '闰年'
    elif y % 400 == 0:
        return '闰年'
    else:
        return '平年'

a = year(1024)
print(a)
b = year(1900)
print(b)