for c in range(3):
    ball = []
    for i in range(5):
        n = input()
        n = int(n)
        ball.append(n)
    if c == 0:
        m = max(ball)
        print(m)
    else:
        m = min(ball)
        print(m)