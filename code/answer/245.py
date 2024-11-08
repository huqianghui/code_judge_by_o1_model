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
if a == '碱性':
    print('蓝色药水')
if a == '中性':
    print('蓝色药水')
    print('加速剂')

print('next')

b = test(7)
if b == '酸性':
    print('红色药水')
if b == '碱性':
    print('蓝色药水')
if b == '中性':
    print('蓝色药水')
    print('加速剂')