def getAverageScore(data):
    totalScore = 0
    count = 0
    projects = data['data']
    for project in projects:
        totalScore += project['exam']['score']
        count += 1
    averageScore = round(totalScore / count, 2)
    return averageScore

hemu = downloadData('禾木')
score = getAverageScore(hemu)
print('项目检测平均分数:', score)



