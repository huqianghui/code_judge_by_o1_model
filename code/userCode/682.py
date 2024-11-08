ball = []
for i in range(5):
    n = input()
    n = int(n)
    ball.append(n)
m=ball[0]
for i in ball:
    if m<i:
        m=i
print(m)