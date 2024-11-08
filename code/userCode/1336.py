import pandas

data = pandas.read_csv('空气等级数据.csv')

mean1 = data['湿度'].mean()
data['湿度'] = data['湿度'].fillna(mean1)

mean2 = data['气压'].mean()
data['气压'] = data['气压'].fillna(mean2)

mode = data['空气等级'].mode()[0]
data['空气等级'] = data['空气等级'].fillna(mode)

# =======将两列字符串特征进行数值化=======
# 风向列值: ["东北风", "西北风", "东南风", "西南风"]
data['风向'] = data['风向'].replace(['东北风','西北风','东南风','西南风'],[1,2,3,4])
# 季节列值: ["春", "夏", "秋", "冬"]
data['季节'] = data['季节'].replace(['春','夏','秋','冬'],[1,2,3,4])

print(data.info())
