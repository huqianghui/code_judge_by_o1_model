numbers = input().split()
int_sum = 0    # 记录整数的总重量
float_sum = 0  # 记录小数的总重量
for x in numbers:
    if '.' in x:
        float_sum += float(x)
    else:
        int_sum += int(x)
print(int_sum, float_sum)