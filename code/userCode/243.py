height = [12, 9, 7, 5]
a = height.index(9)
b = height.index(10)
height.insert(a, 5)
height.insert(b, 6)
tup = tuple(height)
print(tup)