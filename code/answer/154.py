count = 0
for x in books:
    for b in x:
        if '故事' in b:
            print(b)
            count += 1
print(count)
