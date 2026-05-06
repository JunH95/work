# 문제2)
# https://github.com/pykwon/python/tree/master/data
# https://raw.githubusercontent.com/pykwon/python/refs/heads/master/data/train.csv
# 자전거 공유 시스템 분석용 데이터 train.csv를 이용하여 대여횟수에 영향을 주는 변수들을 골라 다중선형회귀분석 모델을 작성하시오.
# 모델 학습시에 발생하는 loss를 시각화하고 설명력을 출력하시오.
# 새로운 데이터를 input 함수를 사용해 키보드로 입력하여 대여횟수 예측결과를 콘솔로 출력하시오.

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# 1. 데이터 로드
url = 'https://raw.githubusercontent.com/pykwon/python/refs/heads/master/data/train.csv'
df = pd.read_csv(url)

# 2. 변수 선택
# datetime은 제외하고 수치형 변수들 중 count에 영향을 줄 것으로 보이는 것들 선택
# casual, registered는 합치면 count가 되므로 제외
features = ['season', 'holiday', 'workingday', 'weather', 'temp', 'humidity', 'windspeed']
target = 'count'

x_data = df[features]
y_data = df[target].values.reshape(-1, 1)

# 3. 데이터 정규화
scaler_x = MinMaxScaler()
x_scaled = scaler_x.fit_transform(x_data)

# target 데이터도 정규화 (선택 사항이지만 성능 향상을 위해 수행)
scaler_y = MinMaxScaler()
y_scaled = scaler_y.fit_transform(y_data)

# 4. 학습/테스트 데이터 분할
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y_scaled, test_size=0.3, random_state=123)

# 5. 모델 구성
model = Sequential([
    Input(shape=(len(features),)),
    Dense(16, activation='relu'),
    Dense(8, activation='relu'),
    Dense(1, activation='linear')
])

model.compile(optimizer='adam', loss='mse', metrics=['mse'])

# 6. 모델 학습
history = model.fit(x_train, y_train, epochs=50, batch_size=32, verbose=1, validation_split=0.2)

# 7. loss 시각화
plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# 8. 설명력(R2 score) 출력
y_pred = model.predict(x_test)
print('\n설명력 (R2 Score):', r2_score(y_test, y_pred))

# 9. 새로운 데이터 예측 (input 함수 사용)
print('\n--- 새로운 데이터 예측 ---')
try:
    # 예시 입력: 1, 0, 1, 1, 20.0, 50, 10.0
    s = int(input('season (1:spring, 2:summer, 3:fall, 4:winter): '))
    h = int(input('holiday (0 or 1): '))
    w_d = int(input('workingday (0 or 1): '))
    wea = int(input('weather (1~4): '))
    t = float(input('temp (e.g. 20.5): '))
    hum = int(input('humidity (0~100): '))
    win = float(input('windspeed (e.g. 10.5): '))

    new_data = np.array([[s, h, w_d, wea, t, hum, win]])
    new_scaled = scaler_x.transform(new_data)
    
    new_pred_scaled = model.predict(new_scaled)
    new_pred = scaler_y.inverse_transform(new_pred_scaled)
    
    print(f'\n예측된 대여 횟수: {new_pred[0][0]:.2f}')
except Exception as e:
    print('입력 오류:', e)
