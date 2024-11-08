def getAverageScore(data):
    totalScore = 0 # 项目检测总分
    count = 0 # 项目检测个数
    projects = data['data']
    for project in projects:
        # 计算项目检测平均分
        totalScore+=projects['']['']
        count+=projects



    return averageScore


hemu = downloadData('桃子')
score = getAverageScore(hemu)
print('项目检测平均分数:', score)



