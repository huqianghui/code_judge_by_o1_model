# 方案C是这样的:
# 投资的第1个月, 利润总额为30元;
# 投资的第2个月, 利润总额为50元;
# 从第3个月开始, 每个月的利润总额是前两个月的利润总额相加之和
# 使用递归的方式编写函数
def compute(n):
    if n==1:
        return 30
    elif n==2:
        return 50
    else:
    # 调用compute()函数, 得到第n-1个月的利润总额, 并将结果返回
    a=compute(n-1)+compute(n-2)
    return a








money = compute(10)
print(money)
