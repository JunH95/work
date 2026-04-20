# 지도학습(KNN) / 비지도학습(Kmeans) 비교 - iris dataset

import imp
from sklearn.datasets import load_iris
iris_data = load_iris()

from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(iris_data.data, iris_data.target, test_size=0.25, random_state=42)

print(train_x.shape, test_x.shape, train_y.shape, test_y.shape)

print("지도학습 - K최근접 이웃 알고리즘")
from sklearn.neighbors import KNeighborsClassifier
knnmodel = KNeighborsClassifier(n_neighbors=3, weights='distance', metric='euclidean')
knnmodel.fit(train_x, train_y)

# 예측 및 성능 확인(accuracy)
pred_label = knnmodel.predict(test_x)
print("예측값 : ", pred_label[:10])
print("실제값 : ", test_y[:10])
from sklearn import metrics
print("분류 정확도 : ", metrics.accuracy_score(test_y, pred_label))

print("\n비지도학습 -k평균 비계층 군집 알고리즘")
from sklearn.cluster import KMeans
kmeansModel = KMeans(n_clusters=3, init='k-means++', n_init=10, random_state=0)
kmeansModel.fit(train_x) # label이 주어지지 않는다

# 군집별 자료보기
print("0 cluster : ", train_y[kmeansModel.labels_ == 0])
print("1 cluster : ", train_y[kmeansModel.labels_ == 1])
print("2 cluster : ", train_y[kmeansModel.labels_ == 2])

# 새로운 값 군집 분류
import numpy as np
new_input = np.array([[6.1, 2.8, 4.7, 1.2]])
pred_cluster = kmeansModel.predict(new_input)
print("새로운 값 군집 분류 : ", pred_cluster)

# 군집 모델 성능 파악
pred_cluster = kmeansModel.predict(test_x)

# 평가 데이터를 적용해 예측한 군집을 각 iris의 종류를 의
# 다시 바꿔줘야 실제 라벨과 비교해 성능 측정 가능

np_arr = np.array(pred_cluster)
np_arr[np_arr == 0] = 2
np_arr[np_arr == 1] = 0
np_arr[np_arr == 2] = 1
print(np_arr)

predict_label = np_arr.tolist()
print(predict_label)
print(f"군집 test acc : {np.mean(predict_label == test_y)}")



