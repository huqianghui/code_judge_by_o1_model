def compute(n):
    if n == 1:
        return 5

    a = compute(n - 1)
    return 2 * a


money = compute(10)
print(money)