s = input().split()
height = [int(i) for i in s]
a = height[0]
height[0] = height[1]
height[1] = a
print(height)