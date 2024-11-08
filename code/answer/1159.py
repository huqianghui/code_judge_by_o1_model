sizes = input()
count = 0  # 统计A级草莓的数量
for x in sizes:
    n = int(x)
    if n > 3:
        count += 1
print(count)
