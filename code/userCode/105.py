def action(x):
    if x == 'red' or x == 'yellow':
        return 'jump'
    elif x == 'biue':
        return 'climb'
    else:
        return 'run'
while True:
    a = input()
    if a == 'brown':
        break
    r = action(a)
    print(r)
