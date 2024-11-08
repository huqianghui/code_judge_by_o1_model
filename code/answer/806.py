def compute(n):
    if n == 1:
        return 30
    elif n == 2:
        return 50
    else:
        a = compute(n - 1) + compute(n - 2)
        return a


money = compute(10)
print(money)
