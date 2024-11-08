blue = ['奶牛', '胆大', '天天']
red = ['天天', '大胆', '肝胆', '牛奶']
for b in blue:
    for r in red:
        p = b + r
        if p[0] == p[3] and p[1] == p[2] and p[0] != p[1]:
            print(p)