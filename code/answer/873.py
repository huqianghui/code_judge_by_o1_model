letters = [['X', 'M', 'R', 'T', 'U', 'H'],
           ['A', 'J', 'F', 'Y', 'M', 'K'],
           ['S', 'L', 'G', 'M', 'R', 'B'],
           ['M', 'C', 'O', 'I', 'E', 'W'],
           ['V', 'B', 'M', 'N', 'F', 'J'],
           ['Z', 'D', 'K', 'U', 'P', 'M']]

for i in range(len(letters)):
    for j in range(len(letters[i])):
        if letters[i][j] == 'M':
            print(i, j)
