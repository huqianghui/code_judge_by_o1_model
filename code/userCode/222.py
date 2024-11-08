def func(n):
    # 调用func函数, 得到第n-1个同学的座位号, 并将这个值存到变量a中
    a = func(n-1) 
    # 给变量a加上1, 得到第n个同学的座位号, 并将结果返回
    return(a+1)


seat = func(4)
print(seat)                                                                                                                                                                             