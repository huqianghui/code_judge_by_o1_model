def test(ph):
    if ph < 7:
        return '酸性'
    elif ph > 7:
        return '碱性'
    else:
        return '中性'

a = test(7)
if a == '酸性':
    print('红色药水')
else:
    print('蓝色药水')
print('next')
b = test(2)
if b == '酸性':
    print('红色药水')
else:
    print('蓝色药水')
