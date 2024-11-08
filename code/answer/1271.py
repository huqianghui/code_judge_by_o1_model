# 编写代码,定义move()函数.
def move(n):
    if n > 9:
        return
    print(n)
    print('left')
    move(n * 3)

# 调用move()函数并传入参数.
move(1)
# 打印'get',收集能量核心.
print('get')