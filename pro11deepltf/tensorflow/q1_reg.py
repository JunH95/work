# =============================================================================
# Galton 데이터셋: 아버지 키로 아들 키 예측하는 다중선형회귀 모델
# =============================================================================
# 데이터셋 출처: https://raw.githubusercontent.com/data-8/materials-fa17/master/lec/galton.csv
#
# 데이터셋 설명:
# - 1886년 영국의 Galton 가족 신장 데이터
# - "평균으로의 회귀(Regression to the Mean)" 개념을 설명하는 고전 데이터셋
#
# 컬럼 정보:
#   - family: 가족 ID
#   - father: 아버지 키 (인치)
#   - mother: 어머니 키 (인치)
#   - midparentHeight: 부모 평균 키 (인치)
#   - children: 가족의 자녀 수
#   - childNum: 자녀 순번
#   - gender: 자녀 성별 (male/female)
#   - childHeight: 자녀의 키 (인치)
# =============================================================================

# 필요한 라이브러리 임포트
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Input
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# =============================================================================
# 1. 데이터 로드 및 전처리
# =============================================================================
# galton.csv 파일을 pandas DataFrame으로 읽어옵니다.
# 이 데이터는 1886년 영국의 Galton 가족 신장 데이터입니다.
data_url = 'https://raw.githubusercontent.com/data-8/materials-fa17/master/lec/galton.csv'
data = pd.read_csv(data_url)

# 데이터 확인 (상위 5개 행 출력)
print("=== 원본 데이터 확인 ===")
print(data.head())
print(f"\n데이터 shape: {data.shape}")
print(f"\n컬럼 목록: {data.columns.tolist()}")

# =============================================================================
# 2. 데이터 필터링 및 전처리
# =============================================================================
# 아들(childHeight)만 예측하므로 gender가 'male'인 데이터만 필터링합니다.
# father(아버지 키)를 특성(feature)으로, childHeight(아들 키)를 정답(label)으로 사용합니다.
data_male = data[data['gender'] == 'male'].copy()
print(f"\n=== male 데이터만 필터링 ===")
print(f"필터링 후 데이터 shape: {data_male.shape}")

# feature(X): 아버지 키 (father)
# label(y): 아들 키 (childHeight)
X = data_male[['father']].values  # 2D array로 변환
y = data_male[['childHeight']].values

print(f"\nX (father) shape: {X.shape}")
print(f"y (childHeight) shape: {y.shape}")

# =============================================================================
# 3. 데이터 정규화 (스케일링)
# =============================================================================
# feature 간 단위의 차이가 크거나 범위가 다르면 모델 성능에 영향을 미칠 수 있습니다.
# MinMaxScaler를 사용하여 0~1 범위로 정규화합니다.
scaler_X = MinMaxScaler(feature_range=(0, 1))
scaler_y = MinMaxScaler(feature_range=(0, 1))

X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y)

print("\n=== 정규화 후 데이터 ===")
print(f"X_scaled 범위: [{X_scaled.min():.4f}, {X_scaled.max():.4f}]")
print(f"y_scaled 범위: [{y_scaled.min():.4f}, {y_scaled.max():.4f}]")

# =============================================================================
# 4. train/test 데이터 분리
# =============================================================================
# sklearn의 train_test_split을 사용하여 데이터를 훈련 세트와 테스트 세트로 분리합니다.
# test_size=0.3: 전체 데이터의 30%를 테스트 세트로 사용
# random_state=123: 재현 가능한 결과를 위해 난수 시드 고정
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_scaled, 
    test_size=0.3, 
    random_state=123
)

print(f"\n=== train/test 분리 결과 ===")
print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}")

# =============================================================================
# 5. Sequential API를 사용한 모델 생성
# =============================================================================
# Sequential API는 층을 순차적으로 쌓는 간단한 방식입니다.
# - Input: father (1개의 특성)
# - Dense(16, activation='relu'): 16개의 뉴런을 가진 은닉층, ReLU 활성화 함수
# - Dense(8, activation='relu'): 8개의 뉴런을 가진 은닉층
# - Dense(1, activation='linear'): 출력층, 회귀이므로 linear 활성화 함수

model_seq = Sequential([
    Input(shape=(1,)),                    # 입력층: 1개의 특성 (father)
    Dense(units=16, activation='relu'),   # 은닉층 1: 16개 뉴런
    Dense(units=8, activation='relu'),    # 은닉층 2: 8개 뉴런
    Dense(units=1, activation='linear')   # 출력층: 1개 출력 (childHeight 예측값)
])

# 모델 컴파일
# - loss: 손실 함수로 MSE (Mean Squared Error) 사용
# - optimizer: Adam 옵티마이저 사용
# - metrics: 평가 지표로 MSE 사용
model_seq.compile(
    loss='mse',
    optimizer='adam',
    metrics=['mse']
)

# 모델 구조 출력
print("\n=== Sequential API 모델 구조 ===")
model_seq.summary()

# =============================================================================
# 6. Sequential API 모델 학습
# =============================================================================
# - epochs: 전체 훈련 데이터를 100번 반복하여 학습
# - batch_size: 한 번에 32개의 샘플을 처리
# - verbose: 학습 과정 출력 (2: 에포크마다 한 줄씩)
# - validation_split: 훈련 데이터의 20%를 검증 데이터로 사용
history_seq = model_seq.fit(
    X_train, y_train,
    epochs=100,
    batch_size=32,
    verbose=2,
    validation_split=0.2
)

# =============================================================================
# 7. Sequential API 모델 평가
# =============================================================================
# 테스트 세트로 모델 평가 (손실과 MSE 계산)
# evaluate는 [loss, metrics] 리스트를 반환합니다.
eval_result_seq = model_seq.evaluate(X_test, y_test, verbose=0)
print(f"\n=== Sequential API 모델 평가 결과 ===")
print(f"Test Loss (MSE): {eval_result_seq[0]:.6f}")
print(f"Test MSE: {eval_result_seq[1]:.6f}")

# =============================================================================
# 8. Functional API를 사용한 모델 생성
# =============================================================================
# Functional API는 더 유연한 모델 구조를 만들 수 있습니다.
# 각 층을 정의하고 입력과 출력을 명시적으로 연결합니다.

# 입력층 정의 (shape=(1,)은 1개의 특성을 의미)
inputs = Input(shape=(1,), name='input_layer')

# 은닉층 1: 16개 뉴런, ReLU 활성화 함수
x = Dense(units=16, activation='relu', name='hidden_layer1')(inputs)

# 은닉층 2: 8개 뉴런, ReLU 활성화 함수
x = Dense(units=8, activation='relu', name='hidden_layer2')(x)

# 출력층: 1개 출력, linear 활성화 함수
outputs = Dense(units=1, activation='linear', name='output_layer')(x)

# 모델 정의: 입력층과 출력층을 연결
model_func = Model(inputs=inputs, outputs=outputs, name='functional_model')

# 모델 컴파일 (Sequential과 동일한 설정)
model_func.compile(
    loss='mse',
    optimizer='adam',
    metrics=['mse']
)

# 모델 구조 출력
print("\n=== Functional API 모델 구조 ===")
model_func.summary()

# =============================================================================
# 9. Functional API 모델 학습
# =============================================================================
history_func = model_func.fit(
    X_train, y_train,
    epochs=100,
    batch_size=32,
    verbose=2,
    validation_split=0.2
)

# =============================================================================
# 10. Functional API 모델 평가
# =============================================================================
eval_result_func = model_func.evaluate(X_test, y_test, verbose=0)
print(f"\n=== Functional API 모델 평가 결과 ===")
print(f"Test Loss (MSE): {eval_result_func[0]:.6f}")
print(f"Test MSE: {eval_result_func[1]:.6f}")

# =============================================================================
# 11. 학습 결과 시각화 (train/test MSE)
# =============================================================================
# matplotlib을 사용하여 훈련 중 손실값 변화를 시각화합니다.
# - loss: 훈련 데이터의 손실
# - val_loss: 검증 데이터의 손실

plt.figure(figsize=(10, 5))

# Sequential API 결과 시각화
plt.subplot(1, 2, 1)
plt.plot(history_seq.history['loss'], label='Train Loss', color='blue')
plt.plot(history_seq.history['val_loss'], label='Validation Loss', color='orange')
plt.title('Sequential API - Loss Visualization')
plt.xlabel('Epoch')
plt.ylabel('Loss (MSE)')
plt.legend()
plt.grid(True)

# Functional API 결과 시각화
plt.subplot(1, 2, 2)
plt.plot(history_func.history['loss'], label='Train Loss', color='blue')
plt.plot(history_func.history['val_loss'], label='Validation Loss', color='orange')
plt.title('Functional API - Loss Visualization')
plt.xlabel('Epoch')
plt.ylabel('Loss (MSE)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# =============================================================================
# 12. 새로운 아버지 키로 아들 키 예측
# =============================================================================
# 학습된 모델을 사용하여 새로운 아버지 키에 대한 아들 키를 예측합니다.
# 예: 아버지 키가 70인치인 경우

new_father_height = 70  # 새로운 아버지 키 (인치)

# 정규화 적용
new_father_scaled = scaler_X.transform([[new_father_height]])

# 예측 (Sequential API 모델 사용)
predicted_child_height_scaled = model_seq.predict(new_father_scaled, verbose=0)

# 역정규화 (원래 스케일로 변환)
predicted_child_height = scaler_y.inverse_transform(predicted_child_height_scaled)

print(f"\n=== 예측 결과 ===")
print(f"아버지 키: {new_father_height} 인치")
print(f"예상 아들 키: {predicted_child_height[0][0]:.2f} 인치")
print(f"예상 아들 키 (cm): {predicted_child_height[0][0] * 2.54:.2f} cm")

# Functional API 모델로도 예측 (비교)
predicted_child_height_func_scaled = model_func.predict(new_father_scaled, verbose=0)
predicted_child_height_func = scaler_y.inverse_transform(predicted_child_height_func_scaled)
print(f"\nFunctional API 예측 결과: {predicted_child_height_func[0][0]:.2f} 인치")

# =============================================================================
# 13. 요약
# =============================================================================
print("\n" + "="*60)
print("요약: Galton 데이터로 아버지 키 예측 모델")
print("="*60)
print(f"1. 데이터: 1886년 Galton 가족 신장 데이터 (아버지-아들 키)")
print(f"2. 사용된 특성: father (아버지 키)")
print(f"3. 예측 대상: childHeight (아들 키)")
print(f"4. 데이터 크기: {len(data_male)}개 (male만)")
print(f"5. train/test 분리: 70%/30%")
print(f"6. Sequential API Test MSE: {eval_result_seq[1]:.6f}")
print(f"7. Functional API Test MSE: {eval_result_func[1]:.6f}")
print(f"8. 아버지 키 {new_father_height}인치 → 예상 아들 키: {predicted_child_height[0][0]:.2f}인치")
print("="*60)

