# 编写代码,定义move()函数.
def move(n):
    if n == 16:
        print(n)
        print('right')
        move(n * 2)
        return
move(1)
print('get')