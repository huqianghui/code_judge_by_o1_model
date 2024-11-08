import pandas as pd
from sklearn.cluster import KMeans


data = pd.read_csv('未知病毒.csv')
x = data.drop(columns=['编号', '宿主', '录入员编号', '录入时间'])
# 创建KMeans模型
cluster=KMeans(n_clusters=3)
# 训练模型
cluster.fit(x)
# 模型预测
result=cluster.predict
# 打印预测结果
print(result)