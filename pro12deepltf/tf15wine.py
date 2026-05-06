# 와인의 등급과 맛 산도 등을 측정해 레트 화이트 분류기 작성

import pandas as pd
from dask.dataframe.methods import loc
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os

wdf = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/wine.csv')
print(wdf.head())
print(wdf.info())
print(wdf.iloc[:, 12].unique())
print(len(wdf[wdf.iloc[:, 12] == 0]))
print(len(wdf[wdf.iloc[:, 12] == 1]))

# array로 변환
dataset = wdf.values
x = dataset[:, 0:12]
y = dataset[:, -1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=12, stratify=y)

# 모델 
model = Sequential()
model.add(Input(shape=(12, )))
model.add(Dense(units=24, activation='relu'))
model.add(Dense(units=12, activation='relu'))
model.add(Dense(units=6, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))
print(model.summary())

model.compile(loss ='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
loss, acc = model.evaluate(x_test, y_test, verbose=0)
print(f'훈련되지 않은 모델의 정확도: {acc * 100}%')

# 조기 종료
early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True) 

#모델 저장
MODEL_DIR = './winemodel/'
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)

# 조건 설정
modelpath = 'winemodel/best_model.keras'
chkpoint = ModelCheckpoint(filepath=modelpath, monitor='val_loss', save_best_only=True, mode='auto')


# 학습 모델
history = model.fit(x_train, y_train, epochs=1000, validation_split=0.2, batch_size=64, callbacks=[early_stop, chkpoint])
loss, acc = model.evaluate(x_test, y_test, verbose=0)
print(f'훈련된 모델의 정확도: {acc * 100}%')

#시각화
epoch_len = history.epoch
plt.plot(epoch_len, history.history['val_loss'], c='red', label='val_loss')
plt.plot(epoch_len, history.history['accuracy'], c='blue', label='accuracy')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend()
plt.grid()
plt.show()

# 저장된 모델로 예측
from tensorflow.keras.models import load_model
mymodel = load_model(modelpath)
new_data = x_test[:5, :]
print(new_data)
new_pred = mymodel.predict(new_data)
print('예측 결과 : ', np.where(new_pred >= 0.5, 1, 0).ravel())


