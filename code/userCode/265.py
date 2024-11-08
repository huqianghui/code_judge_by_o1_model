s = input().split() #把输入拆分成列表
height = [int(i) for i in s] #把列表元素转换成数字
height1=height[0]
height[0]=height[1]
height[1]=height1

print(height)