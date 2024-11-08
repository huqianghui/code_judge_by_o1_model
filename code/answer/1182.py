count = 0
for x in books:
    for b in x:
        if '百科' in b:
            print(b)
            count += 1
print(count)
