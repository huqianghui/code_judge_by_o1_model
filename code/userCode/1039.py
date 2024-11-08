import pandas

df = pandas.read_csv('缺损数据.csv')
body = df['身长']
food = df['日均食量']
# 使用关系式计算缺损的体重数据, 并打印出来
for i in range(len(food)):
    pre =0.1 * df + 9*df -12
    print(pre)