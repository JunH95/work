# 비선형회귀분석

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = np.array([1,2,3,4,5])
y = np.array([4,2,1,3,7])

plt.scatter(x,y)
plt.show()
print(np.corrcoef(x,y)[0,1])

# 선형회귀모델 적용
from sklearn.linear_model import LinearRegression
x = x[:, np.newaxis]  # 차원확대 1차원 -> 2차원 
model = LinearRegression().fit(x,y)
ypred = model.predict(x)
print("예측값 y :", ypred)
print("결정계수 : ", r2_score(y, ypred))

plt.scatter(x,y)
plt.plot(x, ypred, c="red")
plt.show()


# 비선형 모델 작성
# 여러 방법 중 가장 일반적인 방법을 사용
from sklearn.preprocessing import PolynomialFeatures # 다항식 특징 추가
poly = PolynomialFeatures(degree=2, include_bias=False)
x2 = poly.fit_transform(x)
print(x)
print(x2)

model2 = LinearRegression().fit(x2,y)
ypred2 = model2.predict(x2)

plt.scatter(x,y)
plt.plot(x, ypred2, c="red")
plt.show()