blue = ['奶牛', '胆大', '天天']
red = ['天天', '大胆', '肝胆', '牛奶']
for b in blue:
    for r in red:
        n = b + r
        if n[0] == n[3] and n[1] == n[2] and n[0] != n[1]:
            print(n)