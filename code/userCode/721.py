numbers = [[71, 24, 18, 38, 10, 23],
           [5, 35, 30, 6, 65, 87],
           [17, 42, 15, 35, 88, 77],
           [83, 18, 38, 52, 66, 45],
           [49, 40, 16, 2, 28, 21]]
# 第一个线索: 奇数
# 找到每个奇数格子, 打印格子的索引显示内容, 获得新线索
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if numbers[i][j]%2!=0:
            print(i,j)
 