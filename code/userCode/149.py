numbers = input().split()
# 大嘴花的重量都是不同的(有整数, 也有小数), 输入数据中多了一些重复的重量值
numbers2=set(numbers)
s=0
for x in numbers2:
    s+=float(x)
    
print(s)