## 계층적 군집분석
# 학생 10명의 시험점수 사용

from pro9ML.ex2unsuper2cl import x_positions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.cluster import KMeans

students = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10']
scores = np.array([76, 95, 65, 85, 60, 92, 55, 88, 83, 72]).reshape(-1, 1) # 열 하나 행은 알아서 판단하는걸로....
print('점수 : ', scores)

# k=3
kmeans = KMeans(n_clusters=3,init="k-means++", random_state=0)
km_clusters = kmeans.fit_predict(scores)
print("예측 : ", km_clusters)

df = pd.DataFrame({'students' : students, 'scores' : scores.ravel(), 'cluster' : km_clusters})
print(df)

# 군집별 평균 점수는 
print("\n군집별 평균 점수는 ")
grouped = df.groupby('cluster')['scores'].mean()
print(grouped)

# 시각화
x_positions = np.arange(len(students))
y_scores = scores.ravel()
colors = {1:'red', 2:'blue', 3:'green'}
plt.figure(figsize=(10, 6))

# 학생별 군집 색으로 구분해 산점도 출력
for i, (x, y, cluster) in enumerate(zip(x_positions, y_scores, km_clusters)):
    plt.scatter(x, y, color=colors[cluster], s=100)
    plt.text(x, y + 1.5, students[i], fontsize=12, ha='center')

# 중심점
centers = kmeans.cluster_centers_
for center in centers:
    plt.scatter(len(students)//2, center[0], c='black', marker='x', s=200)

plt.xticks(x_positions, students)
plt.xlabel('Students')
plt.ylabel('Score')
plt.title('score cluster')
plt.grid(True)
plt.show()