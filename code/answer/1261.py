count = 0
for x in books:
    for b in x:
        if b == '百科全书1' or b == '百科全书2':
            count += 1
print(count)
