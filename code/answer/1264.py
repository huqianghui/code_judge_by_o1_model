level = {'电流扩大器': 10, '硬盘': 4, '发射枪筒': 3, '螺丝': 1, '特制扳机': 5, 'cpu': 10}
for i in level:
    if level[i] == 10:
        level[i] = '高级'
    elif level[i] == 1:
        level[i] = '低级'
    else:
        level[i] = '中级'
print(level)
