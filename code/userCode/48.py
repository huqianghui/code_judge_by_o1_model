import pandas

data = pandas.read_csv('电影数据.csv')
data = data.drop(columns=['电影名称'])

# 读取电影类型喜爱度, 将'类型'特征数值化
info1 = pandas.read_csv('电影类型喜爱度.csv')
category = list(info1['类型'])
poll = list(info1['喜爱度'])
data['类型'] = data['类型'].replace(category, poll)

# 读取人物喜爱度
info2 = pandas.read_csv('人物喜爱度.csv')
name = list(info2['姓名'])
like = list(info2['喜爱度'])


# 人名存储在变量name中,对应的喜爱度存储在变量like中
# 编写代码,将 '导演' 这一列特征中的人名替换为喜爱度
data['导演'] = 
# 编写代码,将 '编剧' 这一列特征中的人名替换为喜爱度
data['编剧'] = 
# 编写代码,将 '主演' 这一列特征中的人名替换为喜爱度
data['主演'] = 

print(data)




