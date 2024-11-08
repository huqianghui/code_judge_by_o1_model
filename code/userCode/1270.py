# 方案A是这样的:
# 投资的第1个月, 利润总额为5元;
# 每过一个月, 利润总额都是上一个月的2倍
# 使用递归的方式编写函数
def compute(n):
    # 为函数设置结束条件
     if n==1:
        return 5
    a=compute(n-1) 
    return a*2
    

    # 调用compute()函数, 得到第n-1个月的利润总额, 并将结果返回



money = compute(10)
print(money)