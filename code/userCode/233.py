height = [12, 9, 7, 5]
a =height.index(9)
height.insert(a, 10)

b = height.index(5)
height.insert(a, 10)
height.insert(b, 6)
tup = tuple(height)
print(tup)