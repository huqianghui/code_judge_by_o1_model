# 编写代码,定义fix()函数,使用递归的方式打印破损区域的编号.
def fix(n):
    print(n)
    fix(n * 3)

fix(3)