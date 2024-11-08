def compute(n):
    if n == 1:
        return 50
    if n == 2:
        return 100
    a = compute(n - 2)
    return 500 + a


money = compute(10)
print(money)
