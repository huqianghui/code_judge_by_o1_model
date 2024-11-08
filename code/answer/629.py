for i in range(4):
    for j in range(len(books[i])):
        if books[i][j] == '百科全书1' or books[i][j] == '百科全书2':
            print(i + 1, j + 1)
