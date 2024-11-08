import pandas

# 分析 比赛记录.csv 中的数据, 编写代码对成绩进行预测
# 计算平均误差, 根据误差大小调整参数, 使预测误差最小

data = pandas.read_csv('比赛记录.csv')
number = data['题目数量']

pre_score = []
real_score = data['分数']

for x in number:
    y = 10 * x
    pre_score.append(y)


# 通过数据长度获取数据量
num = len(pre_score)
s = 0
for i in range(num):
    if pre_score[i] >= real_score[i]:
        s += pre_score[i] - real_score[i]
    else:
        s += real_score[i] - pre_score[i]

print('平均误差:', s / num)

