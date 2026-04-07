# linearRegressin 클래스 사용
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, explained_variance_score, mean_squared_error
from sklearn.preprocessing import MinMaxScaler

# 데이터 생성
sample_size = 100
np.random.seed(1)

x = np.random.normal(0,10,sample_size)
y = np.random.normal(0,10,sample_size) + x*30

# 독립변수 x를 정규화하기(0~1 사이의 범위 내 자료로 변환)
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x.reshape(-1,))