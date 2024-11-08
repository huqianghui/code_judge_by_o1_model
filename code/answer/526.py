import pandas as pd
from sklearn.cluster import KMeans


data = pd.read_csv('未知病毒.csv')
x = data.drop(columns=['编号', '宿主', '录入员编号', '录入时间'])
cluster = KMeans(n_clusters=3)
cluster.fit(x)
result = cluster.predict(x)
print(result)