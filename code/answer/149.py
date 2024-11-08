numbers = input().split()
weights = set(numbers)
s = 0
for x in weights:
    s += float(x)
print(s)