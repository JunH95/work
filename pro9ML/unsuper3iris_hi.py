# 계층적 군집분석 : 데이터를 단계적으로 묶어 군집을 형성하는 알고리즘
# 거리가 가까운 데이터부터 계속 묶어가는 방식
# 군집 수를 미리 정하지 않아도 됨. 구조는 덴드로그램으로 확인

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster

iris = load_iris()
x = iris.data
y = iris.target
labels = iris.feature_names

# print('x : ', x)
# print('y : ', y)
# print('labels : ', labels)

df = pd.DataFrame(x, columns=labels)
print(df.head(3))

# 스케일링 - 권장!!(군집화는 거리를 기반으로 계산해서 스케일링 중요)
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# 계층적 군집
z = linkage(x_scaled, method='ward')

# 덴드로그램
plt.figure(figsize=(12, 5))
dendrogram(z)
plt.title('iris로 계층적 군집')
plt.xlabel('sample data')
plt.ylabel('유클리디안 거리')
plt.show()

# 덴드로그램을 잘라서 최대 3개의 군집 만들기
clusters = fcluster(Z=z, t=3, criterion='maxclust')

df['cluster'] = clusters
print(df.head(3))
print(df.tail(3))

# 2개 feature 시각화 (산점도)
plt.figure(figsize=(6, 5))
sns.scatterplot(x=x_scaled[:, 0], y=x_scaled[:, 1], hue=clusters, palette='Set1')
# hue = clusters : 군집결과에 따라 색을 달리 표시, palette='Set1' : 색상 스타일 지정
plt.title('군집결과')
plt.xlabel('feature1')
plt.ylabel('feature2')
plt.show() # 꽤 비슷하게 나눠짐. 군집은 정답 라벨이 없음

print('실제 label : ', y[:10])          # 실제 label :  [0 0 0 0 0 0 0 0 0 0]
print('예측 label : ', clusters[:10])   # 예측 label :  [1 1 1 1 1 1 1 1 1 1]   -> 실제 0이 군집 1로 군집화됨

print('군집 결과 검증')
print('교차표 - 실제 라벨 vs 군집 결과')
ct = pd.crosstab(y, clusters)
print('ct : \n', ct)