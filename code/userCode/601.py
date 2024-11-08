# 方案B是这样的:
# 投资的第1个月, 利润总额为50元;
# 投资的第2个月, 利润总额为100元;
# 从第3个月开始, 第n个月的利润总额比第n-2个月多500元
# 使用递归的方式编写函数
def compute(n):
    if n==1:
        return 50
    if n==2:
        return 100
    a=compute(n-2)
    return + 500
money = compute(10)
print(money)
