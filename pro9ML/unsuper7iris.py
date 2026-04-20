# kmeans : iris dataset 군집분석 정량평가 클러스터별 평균비교(ANOVA)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score, silhouette_score
# adjusted_rand_score : 군집 vs 실제 라벨 비교
# normalized_mutual_info_score : 정보량 기반 유사도(같은 정보 공유)
# silhouette_score : 군집 자체 품질 평가(군집에 잘 속해 있는가 확인)
from sklearn.decomposition import PCA  # 4차원 2차원으로 축소
import os 
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE' 

iris = load_iris()
x = iris.data
y = iris.target
feature_names = iris.feature_names

df = pd.DataFrame(x, columns=feature_names)
print(df.head(3))

# 스케일링 
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# kmeans 모델
k=3
kmeans = KMeans(n_clusters=k, init='k-means++', n_init=10, random_state=42)
clusters = kmeans.fit_predict(x_scaled)
df['cluster'] = clusters

# pca
pca = PCA(n_components=2)
x_pca = pca.fit_transform(x_scaled)
print('pca 설명 분산 비율 : ', pca.explained_variance_ratio_)

plt.figure(figsize=(6,5))
sns.scatterplot(x=x_pca[:, 0], y=x_pca[:, 1], hue=clusters, palette='Set1')
plt.title('iris 군집결과')
plt.xlabel('pca1')
plt.ylabel('pca2')
plt.show()

# 실제 라벨과 군집 비교
ct = pd.crosstab(y, clusters)
print('교차표 : \n', ct)

# 정량적 평가
ari = adjusted_rand_score(y, clusters)
nmi = normalized_mutual_info_score(y, clusters)
sil = silhouette_score(x_scaled, clusters)

print(f'ARI : {ari:.4f}')
print(f'NMI : {nmi:.4f}')
print(f'Silhouette Score : {sil:.4f}')

initia = []
k_range = range(1, 10)
for k in k_range:
    km = KMeans(n_clusters=k, init='k-means++', n_init=10, random_state=42)
    km.fit(x_scaled)
    initia.append(km.inertia_)

plt.figure(figsize=(6,4))
plt.plot(k_range, initia, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('SSE')
plt.show()

# 실제 vs 군집 비교 시각화
plt.figure(figsize=(12, 5))
# 실제 라벨
plt.subplot(1, 2, 1)
sns.scatterplot(x=x_pca[:, 0], y=x_pca[:, 1], hue=y, palette='Set2')
plt.title('Actual Labels')
plt.xlabel('PCA1')
plt.ylabel('PCA2')

plt.subplot(1, 2, 2)
sns.scatterplot(x=x_pca[:, 0], y=x_pca[:, 1], hue=clusters, palette='Set1')
plt.title('KMeans Clusters')
plt.xlabel('PCA1')
plt.ylabel('PCA2')

plt.show()

# 클러스터별 평균 분석
pd.set_option('display.max_columns', None)
print(df.groupby('cluster')[feature_names].mean())

# 군집 3개 : 군집 간 평균 차이 검정(ANOVA)
# 귀무 : 군집 간 평균에 차이가 없다
# 대립 : 군집 간 평균에 차이가 있다
from scipy.stats import f_oneway

for col in feature_names:
    group1 = df[df['cluster'] == 0][col]
    group2 = df[df['cluster'] == 1][col]
    group3 = df[df['cluster'] == 2][col]
    f_stat, p_val = f_oneway(group1, group2, group3)
    print(f'{col} : F={f_stat:.4f}, p={p_val:.4f}')

# 해석
if p_val >= 0.05:
    print("귀무가설 채택 : 군집 간 평균에 차이가 없다")
else:
    print("귀무가설 기각 : 군집 간 평균에 차이가 있다")

# kmeans 가 꽃받침 꽃임ㅍ 길이 너비를 제대로 군집분석했음을 알 수 있다

# 사후 검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd

for col in feature_names:
    tukey = pairwise_tukeyhsd(endog=df[col], groups=df['cluster'], alpha=0.05)
    print(tukey)

# 사후 검정 시각화
tukey.plot_simultaneous(figsize=(6,4))
plt.title('Tukey HSD')
plt.xlabel('평균차이')
plt.show()

# 군집별 boxplot
for col in feature_names:
    plt.figure(figsize=(5,3))
    sns.boxplot(x='cluster', y=col, data=df)
    plt.title(f'{col} by cluster')
    plt.show()