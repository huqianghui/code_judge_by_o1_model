
def move(n):
    if n==15:
        return
    print(n)
    print('right')
    move(n *2)

move(1)
print('get')
