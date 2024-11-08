count = 0
for i in scores:
    for j in i:
        if j > 90:
            count += 1
print(count)