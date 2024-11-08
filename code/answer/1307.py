'''
AI_data = [['能量体02', 'E', 32, 'AI'],
           ['能量体05', 'E', 50, 'AI'],
           ['能量体07', 'W', 44, 'AI'],
           ......
                                        ]
'''
n = []
m = 0
for x in AI_data:
    if x[2] > m:
        m = x[2]
        n = x
print(m)
print(n)