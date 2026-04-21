# dbscan 이란?
# 머신러닝에 주로 사용되는 클러스터링 알고리즘으로 multi dimension 데이터를 밀도 기반으로 서로 
# 가까운 데이터 포인터를 함께 그룹화하는 알고리즘
# dbscan은 밀도가 다양하거나 모양이 불규칙한 클러스터가 있는 데이터와 같이 모양이
# 잘 정의되지 않고 이상치가 많은 데이터를 처리할 때 유용

import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN, KMeans

# 데이터 생성
x, y = make_moons(n_samples=200, noise=0.05, random_state=0, shuffle=True)

plt.scatter(x[:, 0], x[:, 1], s=30)
plt.show()

print("Kmeans로 군집 분류")
km = KMeans(n_clusters=2, init="k-means++", random_state=0)
pred1 = km.fit_predict(x)

# km 결과 시각화
def plotResult(x, pr):
    plt.scatter(x[pr == 0, 0], x[pr == 0, 1], c='blue', marker='o', s=40, label='Cluster 1')
    plt.scatter(x[pr == 1, 0], x[pr == 1, 1], c='red', marker='s', s=40, label='Cluster 2')
    plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], c='black', marker='+', label='Centroids')
    plt.legend()
    plt.show()

plotResult(x, pred1)

print("DBscan으로 군집 분류")
db = DBSCAN(eps=0.2, min_samples=5, metric='euclidean')  # eps: 샘플간 최대거리, min_samples: 핵심포인트가 되기위한 최소 샘플수
pred2 = db.fit_predict(x)

# db 결과 시각화
def plotResult2(x, pr):
    plt.scatter(x[pr == 0, 0], x[pr == 0, 1], c='blue', marker='o', s=40, label='Cluster 1')
    plt.scatter(x[pr == 1, 0], x[pr == 1, 1], c='red', marker='s', s=40, label='Cluster 2')
    plt.legend()
    plt.show()

plotResult2(x, pred2)
