from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

x = getData()
# 最大平均轮廓系数
maxSihouette = 0
# 最大平均轮廓系数对应的k值
n = 0
for k in range(3,11):
    # 创建KMeans模型
    cluster = KMeans(n_clusters=k)
    # 训练模型
    cluster.fit(x)
    # 模型预测
    result = cluster.predict(x)
    # 计算平均轮廓系数
    score = silhouette_score(x, result)
    # 比较平均轮廓系数大小
    if score >maxSihouette:
        maxSihouette = score
        n = k

print('化石类别总数为:', n)
print('最大平均轮廓系数为:', maxSihouette)