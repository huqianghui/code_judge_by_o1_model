s = input().split()
height = [int(i) for i in s]
for i in range(4):
    height[i], height[i+1] = height[i+1], height[i]
    print(height)