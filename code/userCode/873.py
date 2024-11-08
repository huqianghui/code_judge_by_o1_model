letters = [['X', 'M', 'R', 'T', 'U', 'H'],
           ['A', 'J', 'F', 'Y', 'M', 'K'],
           ['S', 'L', 'G', 'M', 'R', 'B'],
           ['M', 'C', 'O', 'I', 'E', 'W'],
           ['V', 'B', 'M', 'N', 'F', 'J'],
           ['Z', 'D', 'K', 'U', 'P', 'M']]
# 已获得线索: M
# 找到每个字母是M的格子, 打印格子的索引显示内容, 获得新线索
for i in range(len(letters)):
    for j in range(len(letters[i])):
        if letters[i][j]=='M':
            print(i,j)
        
    