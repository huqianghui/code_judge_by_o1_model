s = input().split()
height = [int(i) for i in s]
for i in range(5):
    for j in range(5):
        if height[j] > height[j+1]:
            height[j], height[j+1] = height[j+1], height[j]
print(height)