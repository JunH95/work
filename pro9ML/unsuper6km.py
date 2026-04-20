# 쇼핑몰 고객 세분화 연습

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.cluster import KMeans

# 가상 고객 데이터 생성
np.random.seed(0)
n_customers = 200
annul_spending = np.random.normal(50000,15000, n_customers) # 연간 지출액
monthly_visits = np.random.normal(5, 2, n_customers) # 월 방문 횟수

# 구간 나누기(음수 제거 - clip)
annul_spending = np.clip(annul_spending, 0, None)
monthly_visits = np.clip(monthly_visits, 0, None)

# 데이터프레임 생성
data = pd.DataFrame({
    'annual_spending' : annul_spending,
    'monthly_visits' : monthly_visits
})

print(data.head())

# 산점도
plt.figure(figsize=(8, 6))
plt.scatter(data['annual_spending'], data['monthly_visits'], c='blue', marker='o', s=50)
plt.xlabel('Annual Spending')
plt.ylabel('Monthly Visits')
plt.title('Customer Segmentation')
plt.grid(True)
plt.show()

# kmeans 군집화
kmeans = KMeans(n_clusters=3, random_state=0)
clusters = kmeans.fit_predict(data)

# 군집결과 시각화
data['cluster'] = clusters

for cluster_id in np.unique(clusters):
    cluster_data = data[data['cluster'] == cluster_id]
    plt.scatter(cluster_data['annual_spending'], cluster_data['monthly_visits'], label=f'Cluster {cluster_id}')

# 중심점
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='black', marker='x', s=200, label='center')
plt.xlabel('Annual Spending')
plt.ylabel('Monthly Visits')
plt.title('Customer Segmentation')
plt.legend()
plt.show()
