def func(n):
    a = func(n - 1)
    return a + 1


seat = func(4)
print(seat)
