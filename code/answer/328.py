name_data = [['王者荣耀', 97978],
             ['香肠派对', 22961], 
             ['我的世界', 50868],
             ['第五人格', 14556],
             ['和平精英', 55671]]

def mykey(x):
    return x[1]

name_data.sort(key=mykey)
print(name_data)