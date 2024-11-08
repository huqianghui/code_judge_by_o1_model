blue = ['嬉嬉', '思考', '痴痴', '哈哈']
red = ['哈嘿', '考古', '痴想', '搞笑', '嬉笑']
for b in blue:
    for r in red:
        p = b + r
        if p[0] == p[1] and p[1] == p[2]:
            print(p)