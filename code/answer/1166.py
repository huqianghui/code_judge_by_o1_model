for c in range(4):
    ball= []
    for i in range(5):
        n = input()
        n = int(n)
        ball.append(n)
    if c==0 or c==1:
        m = min(ball)
        print(m)
    else:
        m = max(ball)
        print(m)
