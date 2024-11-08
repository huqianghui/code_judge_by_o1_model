numbers = input().split()
int_sum = 0    # 记录整数的总重量
float_sum = 0  # 记录小数的总重量
for i in numbers:
    if '.'in i:
        float_sum+=float(i)
    else:
        int_sum+=int(i)
print(int_sum, float_sum)