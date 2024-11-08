gun = {'发射枪筒': 2, '电源': 3, '螺丝': 5}
box1 = {'CPU': 24, '电源': 45, '螺丝': 11, '硬盘': 12, '扳手': 16, '内存卡': 17}
box2 = {'电磁集束弹': 35, '砝码': 45, '摄像头': 23, '发射枪筒': 13, '芯片': 54, '特制扳机': 17}
for i in gun:
    if i in box1:
        box1[i] = box1[i] - gun[i]
    if i in box2:
        box2[i] =box2[i]-gun[i]


print(box1)
print(box2)
