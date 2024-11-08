import pandas

f = pandas.read_csv('players.csv')

# 编写代码,打印禾木的身高
print(f.values[7][3])
# 编写代码,打印桃子的年龄
print(f.values[2][2])
# 编写代码,打印乌拉乎的爱好
print(f.values[4][5])
