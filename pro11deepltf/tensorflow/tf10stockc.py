# 주식데이터로 다중선형회귀 모델 작성
# 전날 데이터로 다음날 종가 예측

from os import write
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Activation
from tensorflow.keras import optimizers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, minmax_scale, MinMaxScaler

# 배열자료로 읽기
datas = np.loadtxt('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/stockdaily.csv', delimiter=',', skiprows=1)
print(datas[:2], len(datas))

# feature
x_data = datas[:, 0:-1]
print(x_data.shape)
scaler = MinMaxScaler(feature_range=(0,1))  # 정규화
x_data = scaler.fit_transform(x_data)
print(x_data[:2])
print(scaler.inverse_transform(x_data[:2]))

# label
y_data = datas[:, -1]  # 종가 
print(y_data[:2])
print()
print(x_data[0], y_data[0])
print(x_data[1], y_data[1])
# x_data 와 y_data를 한 칸씩 어긋나게 맞추기 위한 전처리
x_data = np.delete(x_data, -1, axis=0)
y_data = np.delete(y_data, 0)
print(x_data[0], y_data[0])

print('train / test split 없이 모델 작성')
model = Sequential()
model.add(Input(shape=(4, )))
model.add(Dense(units=1, activation='linear'))
model.compile(loss='mse', optimizer='sgd', metrics=['mse'])
model.fit(x_data, y_data, epochs=200, verbose=0)
print('evaluate result : ', model.evaluate(x_data, y_data, verbose=0))

from sklearn.metrics import r2_score
pred = model.predict(x_data)
print('train / test split 없이 설명력 : ', r2_score(y_data, pred))

# 시각화
plt.plot(y_data, 'b', label='real')
plt.plot(pred, 'r--', label='pred')
plt.legend()
plt.show()

print()
print('train / test split 한 경우 -----------------')
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3, shuffle=False, random_state=123)

model2 = Sequential()
model2.add(Input(shape=(4, )))
model2.add(Dense(units=1, activation='linear'))
model2.compile(loss='mse', optimizer='sgd', metrics=['mse'])
model2.fit(x_train, y_train, epochs=200, verbose=0)
print('evaluate result : ', model2.evaluate(x_test, y_test, verbose=0))

pred2 = model2.predict(x_test)
print(' 설명력 : ', r2_score(y_test, pred2))
#  과적합이 의심스러움

plt.plot(y_test, 'b', label='real')
plt.plot(pred2, 'r--', label='pred')
plt.legend()
plt.show()

# 딥러닝의 이슈 : 최적화와 일반화


