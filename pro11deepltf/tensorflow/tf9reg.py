# 다중선형회귀 : tv, radio, newspaper 광고비에 따른 판매량 예측

from os import write
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Activation
from tensorflow.keras import optimizers
import numpy as np
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/Advertising.csv')
del data['no']
print(data.head(2))

fdata = data[['tv', 'radio', 'newspaper']]
# ldata = data[['Sales']]
ldata = data.iloc[:, [3]]
print(fdata.head(2))
print(ldata.head(2))

# feature 간 단위의 차이가 클 경우 정규화/표준화 작업이 모델 성능에 도움
from sklearn.preprocessing import StandardScaler, minmax_scale, MinMaxScaler

# 정규화
scaler = MinMaxScaler(feature_range=(0,1))
fdata = scaler.fit_transform(fdata)
fdata = minmax_scale(fdata, axis=0, copy=True)  # 행기준, 원본자료 보존

# train / test 분할
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(fdata,ldata, shuffle=True ,test_size=0.3, random_state=123)
# stratify는 회귀에서는 안줌

# 전처리가 모두 끝난 경우 모델 설계 및 실행
model = Sequential()
model.add(Input(shape=(3, )))
model.add(Dense(units=16, activation='relu'))
model.add(Dense(units=8, activation='relu'))
model.add(Dense(units=1, activation='linear')) # activation 생략 가능
print(model.summary())


tf.keras.utils.plot_model(
    model,
    to_file='aaa.png',
    show_shapes=True,
    show_layer_names=True,
    show_dtype=True,
    show_layer_activations=True,
    dpi=96
    )
# 케라스 모델 구조를 이미지 파일로 저장
    
model.compile(loss='mse', optimizer='adam', metrics=['mse'])

history = model.fit(x_train, y_train, epochs=100, batch_size=32, verbose=2, validation_split=0.2)

ev_loss = model.evaluate(x_test, y_test, verbose=0)
print('평가용 loss : ', ev_loss)

# history 값 확인
print('history : ', history.history)
print('history loss : ', history.history['loss'])
print('history mse : ', history.history['mse'])
print('history val_loss : ', history.history['val_loss'])
print('history val_mse : ', history.history['val_mse'])

# loss 시각화
import matplotlib.pyplot as plt
plt.plot(history.history['val_loss'], label='val_loss')
plt.plot(history.history['loss'], label='loss')
plt.show()

from sklearn.metrics import r2_score
print('설명력 : ', r2_score(y_test, model.predict(x_test)))

# predict
pred = model.predict(x_test)
print('예측값 : ', pred.ravel())
print('실제값 : ', y_test.values.ravel())

print('\n\nFunctional api를 사용한 방법--------------')
from tensorflow.keras.models import Model
# 입력층 정의
inputs = Input(shape=(3, ), name='input_layer')
# 은닉층 정의
x = Dense(units=16, activation='relu', name='hidden_layer1')(inputs)
x = Dense(units=8, activation='relu', name='hidden_layer2')(x)
# 출력층 정의
outputs = Dense(units=1, activation='linear', name='output_layer')(x)
# 모델 정의
func_model = Model(inputs=inputs, outputs=outputs)
print(func_model.summary())

func_model.compile(loss='mse', optimizer='adam', metrics=['mse'])

history = func_model.fit(x_train, y_train, epochs=100, batch_size=32, verbose=2, validation_split=0.2)

func_ev_loss = func_model.evaluate(x_test, y_test, verbose=0)
print('func_model ev_loss : ', func_ev_loss)
print('func_model 설명력 : ', r2_score(y_test, func_model.predict(x_test)))

# tensorboard 실행 ----------
# pip install tensorboard
from tensorflow.keras.callbacks import TensorBoard
import datetime
import os

# tensorboard log 저장 경로
log_dir = os.path.join('logs', 'fit', datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
tb = TensorBoard(log_dir=log_dir, histogram_freq=1, write_graph=True, write_images=True)

func_model.fit(x=x_train, y=y_train, epochs=100, batch_size=32, verbose=2, validation_split=0.2, callbacks=[tb])

# 텐서보드 실행 후 결과는 브라우저로 확인
# 터미널 프롬프트에서 > tensorboard --logdir=logs/fit
# 브라우저로 http://localhost:6006/
