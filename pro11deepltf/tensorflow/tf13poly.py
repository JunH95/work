# 다항회귀
# 매출 = 광고비 * w + b
# 매출 = 광고비1 * w1 + 광고비2 * w2 + b  
# 광고비와 매출의 관계가 직선이 아니라 곡선형태의 자료를 대상

# 다항회귀에 적합한 데이터 생성 -> csv 파일로 저장 후 읽기 -> 산점도
# -> train / test split -> 선형모델, 비선형모델 학습 후 성능 비교


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import tensorflow as tf

np.random.seed(7)
tf.random.set_seed(7)

# 광고비가 증가하면 매출도 증가하나, 어느 정도 이후에는 증가율이 둔화됨.
ad_cost = np.linspace(0,100,80)  # 광고비 데이터
# sales는 광고비에 따른 매출 데이터를 만드는 부분 2차함수
# sales = 광고비제곱 * -0.06 + 7.5 * 광고비 + 40 + noise  인위적으로 수식 작성
sales = (-0.06 * ad_cost ** 2) + (7.5 * ad_cost) + 40 + np.random.normal(0,25,size=len(ad_cost))

df = pd.DataFrame({'광고비': ad_cost, '매출':sales})
print(df.head())
df.to_csv('ad_sales.csv',index=False, encoding='utf-8-sig')
print('csv 저장 성공')

df = pd.read_csv('ad_sales.csv')
print(df.info())

# 결측치가 있다면 해당 행 삭제
df = df.dropna()
print(df.shape)

# feature, label 분리
x = df[['광고비']].values.astype(np.float32)
y = df[['매출']].values.astype(np.float32)

print(x.shape, y.shape)
print(x[:3])
print(y[:3])

# 시각화
plt.figure(figsize=(8,5))
plt.scatter(x, y, alpha=0.7)
plt.xlabel('광고비')
plt.ylabel('매출')
plt.title('광고비와 매출의 관계')
plt.grid(True)
plt.show()

# train / test split
indices = np.arange(len(x))
np.random.shuffle(indices)
x = x[indices]
y = y[indices]
train_size = int(len(x) * 0.8)
x_train, x_test = x[:train_size], x[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# scaling : train 데이터 기준으로 평균과 표준편차 계산 후 표준화
x_mean = x_train.mean(axis=0)
x_std = x_train.std(axis=0)
# 표준화
x_train_scaled = (x_train - x_mean) / x_std
x_test_scaled = (x_test - x_mean) / x_std

y_mean = y_train.mean(axis=0)
y_std = y_train.std(axis=0)
# 표준화
y_train_scaled = (y_train - y_mean) / y_std
y_test_scaled = (y_test - y_mean) / y_std

# 다항 특성 함수 : degree = 2이면 [x, x**2] 생성
# 스케일링된 입력값을 다항회귀용 입력 데이터로 변환
def make_polynomial_feature(x_scaled, degree=2):
    features = [x_scaled ** d for d in range(1, degree +1)]
    return np.concatenate(features, axis=1).astype(np.float32)

x_train_poly = make_polynomial_feature(x_train_scaled, degree=2)
x_test_poly = make_polynomial_feature(x_test_scaled, degree=2)
print('선형회귀 입력 shape : ', x_train_scaled.shape)
print('다항회귀 입력 shape : ', x_train_poly.shape)
print(x_train_poly[:2])
print(x_test_poly[:2])

# r2 score 함수 정의
def r2_score(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred)**2)
    ss_tot = np.sum((y_true - y_true.mean())**2)
    return 1 - (ss_res / ss_tot)

# 모델 성능 평가 함수
def evaluate_model(name, y_true, y_pred):
    mse = np.mean((y_true - y_pred)**2)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)
    print(f'\n[{name}]')
    print('mse : ', round(mse,3))
    print('rmse : ', round(rmse,3))
    print('r2 : ', round(r2,3))

# 선형회귀 모델 
linear_model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),
    tf.keras.layers.Dense(units=1)
])

linear_model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01), loss='mse')
linear_model.fit(x_train_scaled, y_train_scaled, epochs=2000, verbose=0)

y_pred_linear_scaled = linear_model.predict(x_test_scaled, verbose=0)
# 원래 매출 단위로 예측값 복원
y_pred_linear = y_pred_linear_scaled * y_std + y_mean

# 다항회귀 모델 
poly_model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(2,)),
    tf.keras.layers.Dense(units=1)
])

poly_model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01), loss='mse')
poly_model.fit(x_train_poly, y_train_scaled, epochs=2000, verbose=0)

y_pred_poly_scaled = poly_model.predict(x_test_poly, verbose=0)
# 원래 매출 단위로 예측값 복원
y_pred_poly = y_pred_poly_scaled * y_std + y_mean

# 성능비교
evaluate_model('선형회귀 모델', y_test, y_pred_linear)
evaluate_model('다항회귀 모델', y_test, y_pred_poly)

# 시각화
x_plot = np.linspace(x.min(), x.max(), 300).reshape(-1, 1).astype(np.float32)
# 스케일링
x_plot_scaled = (x_plot - x_mean) / x_std
# 다항특성 변환
x_plot_poly = make_polynomial_feature(x_plot_scaled, degree=2)

# 예측
y_plot_linear_scaled = linear_model.predict(x_plot_scaled, verbose=0)
y_plot_poly_scaled = poly_model.predict(x_plot_poly, verbose=0)

# 매출 복원
y_plot_linear = y_plot_linear_scaled * y_std + y_mean
y_plot_poly = y_plot_poly_scaled * y_std + y_mean

plt.figure(figsize=(9,6))
plt.scatter(x_train, y_train, label='훈련데이터', alpha=0.5)
plt.scatter(x_test, y_test, label='테스트데이터', alpha=0.9)
plt.plot(x_plot, y_plot_linear, color='red', label='선형회귀')
plt.plot(x_plot, y_plot_poly, color='green', label='다항회귀')
plt.xlabel('광고비')
plt.ylabel('매출')
plt.title('선형회귀 vs 다항회귀')
plt.legend()
plt.grid(True)
plt.show()


