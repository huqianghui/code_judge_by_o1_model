def test(ph):
    if ph < 7:
        return '酸性'
    elif ph > 7:
        return '碱性'
    else:
        return '中性'
a = test(3)
if a == '酸性':
    print('红色药水')
elif a == '碱性':
    print('蓝色药水')
else:
    print('蓝色药水')
    print('加速剂')
a = test(7)
if a == '酸性':
    print('红色药水')
else a == '碱性':
    print('蓝色药水')
else:
    print('蓝色药水')
    print('加速剂')