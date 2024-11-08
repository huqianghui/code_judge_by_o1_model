chipsL = ['祖冲之核晶', '香农核晶', '笛卡尔核晶', '艾兹格核晶'] 
chipsR = ['布尔核晶', '图灵核晶']
for i in range(5):
    print('scan')
    a = input()
    if a in chipsR:
        print('load','right')
    if a in chipsL:
        print('load','left')    
