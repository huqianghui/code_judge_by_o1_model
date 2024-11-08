import pandas

# 1.读取'通行证.csv'中的内容
f=pandas.read_csv("通行证_csv")

# 2.获取每一列数据
ci=f["磁力"]
hou=f["厚度"]
qing=f["清晰度"]

# 3.分别计算三个特征与检测结果的相关性,并打印出来
a=ci_r=c.corr(result)
b=hou_r=c.corr(result)
c=qing_r=c.corr(result)



print('磁力与检测结果的相关性:',a)
print('厚度与检测结果的相关性:',b)
print('清晰度与检测结果的相关性:',c)





