name_data = [['王者荣耀', 97978],
             ['香肠派对', 22961], 
             ['我的世界', 50868],
             ['第五人格', 14556],
             ['和平精英', 55671]]

def mykey(x):
    #填写代码,设置排序依据为玩家人数
    return x[1]

#填写代码,指定排序的依据
name_data.sort(key=mykey)


print(name_data)