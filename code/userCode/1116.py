info = {'水瓶座': '0120-0218', '双鱼座': '0219-0320', '白羊座': '0321-0419', '金牛座': '0420-0520', '双子座': '0521-0621', '巨蟹座': '0622-0722','狮子座': '0723-0822', '处女座': '0823-0922', '天秤座': '0923-1023', '天蝎座': '1024-1122', '射手座': '1123-1221', '摩羯座': '1222-0119'}
while True:
    d = input('请输入出生日期:')
    if d.isdigit():
        print('出生日期:', d)
        break
    else:
        print('输入的日期有误')
d = int(d)
for i in info:
    t = info[i].split('-')
    t1 = int(t[0])
    t2 = int(t[1])
    if b>=t1 and b<=t2:
        print('你的星座是:',i)
        break