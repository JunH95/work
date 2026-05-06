# 딥러닝으로 이진분류 - 전통적인 방식인 logisticregression 확장

from dask.dataframe.methods import loc
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam
import tensorflow as tf
import numpy as np

np.random.seed(42)
tf.keras.utils.set_random_seed(42)

x_data = np.array([[1,2],[2,3],[3,4],[4,3],[3,2],[2,1]], dtype=np.float32)
y_data = np.array([[0],[0],[0],[1],[1],[1]], dtype=np.float32)

print('1) Sequential API 버전 (빠른 구현)')
# 층을 순서대로 쌓는 단순 구조, 분기 구조나 다중 입출력 불가능
# model = Sequential([
# Input(shape=(2, )
# Dense(units=1), activation='sigmoid)
# ])
model = Sequential()
model.add(Input(shape=(2, )))
model.add(Dense(units=4, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))
print(model.summary())

model.compile(loss ='binary_crossentropy', optimizer=Adam(learning_rate=0.01), metrics=['accuracy'])
model.fit(x_data, y_data, epochs=20,batch_size=1, verbose=0)
m_eval = model.evaluate(x_data, y_data)
print(m_eval)
print(f'평가 결과 : 손실={m_eval[0]:.4f}, 정확도={m_eval[1]:.4f}')
# 손실을 최소화 하기 위해 경사하강법 사용
# z=w•x+b

# 예측값과 실제값으로 시각화(s곡선 형태)
import matplotlib.pyplot as plt
# 2차원 입력(x1, x2)을 가진 모델을 1차원 처럼 만들어 시그모이드를 보기위한 준비
x1_range = np.linspace(0,6,100)
x2_fixed = 2.5

# 입력 데이터 생성, 두 배열을 합쳐서 (x1, x2) 쌍 만들기
x_vis = np.column_stack([x1_range, np.full_like(x1_range, x2_fixed)])
y_prob = model.predict(x_vis, verbose=0)

x1_real = x_data[:,0]
y_real = y_data.ravel()

plt.figure(figsize=(7,5))
plt.plot(x1_range, y_prob, label='sigmoid')
plt.scatter(x1_real, y_real, color='red', label='True data')
plt.xlabel('x_data')
plt.ylabel('probability')
plt.legend(loc='lower right')
plt.grid()
plt.show()

from sklearn.metrics import accuracy_score
pred = model.predict(x_data, verbose=0)
pred_class = (pred >= 0.5).astype(int)
accuracy = accuracy_score(y_data, pred_class)
print(f'1) 정확도 : {accuracy:.4f}')

# 새로운 값으로 분류 예측
new_data = np.array([[1,2],[10,5]])
pred = model.predict(new_data)
print('예측 확률 : ', pred.ravel())

print('예측 결과 : ', (pred >= 0.5).astype(int).ravel())
print('예측 결과 : ', [1 if i >= 0.5 else 0 for i in pred])
print('예측 결과 : ', np.where(pred >= 0.5,1,0).ravel())

print('2) Functional API 버전 (유연한 구조)')  # 실무에서 주로 사용
# 다중 입출력 가능 구조가 유현, 복잡한 모델에 효과적

from tensorflow.keras.models import Model

inputs = Input(shape=(2, ))
outputs = Dense(units=4, activation='relu')(inputs)
outputs = Dense(units=1, activation='sigmoid')(outputs)
model_func = Model(inputs=inputs, outputs=outputs)

print(model_func.summary())

model_func.compile(loss ='binary_crossentropy', optimizer=Adam(learning_rate=0.01), metrics=['accuracy'])
model_func.fit(x_data, y_data, epochs=20,batch_size=1, verbose=0)
m_eval2 = model_func.evaluate(x_data, y_data)
print(m_eval2)
print(f'평가 결과2 : 손실={m_eval2[0]:.4f}, 정확도={m_eval2[1]:.4f}')

print('3) Functional API 버전2(다중 입력)')
# 이전 : [x1, x2] -> dense -> dense -> 출력
# 다중입력 : 입력을 따로 받아 각각 특징을 뽑아 합치는 방식, 각각 따로 전처리 가능 
# x1 -> dense
            # -> concat -> dense -> 출력
# x2 -> dense 
from tensorflow.keras.layers import Concatenate
# 입력 분리
input1 = Input(shape=(1,))
input2 = Input(shape=(1,))
# 각각 처리
x1 = Dense(units=2, activation='relu')(input1)
x2 = Dense(units=2, activation='relu')(input2)
# 합치기
merged = Concatenate()([x1,x2])
output = Dense(units=1, activation='sigmoid')(merged)
multi_model = Model(inputs=[input1, input2], outputs=output)
print(multi_model.summary())

multi_model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.01), metrics=['accuracy'])
# 데이터 분리해서 입력
x1_data = x_data[:, 0].reshape(-1,1)
x2_data = x_data[:, 1].reshape(-1,1)
multi_model.fit([x1_data, x2_data], y_data, epochs=20, batch_size=1, verbose=0)
m_eval3 = multi_model.evaluate([x1_data, x2_data], y_data)
print(m_eval3)
print(f'평가 결과3 : 손실={m_eval3[0]:.4f}, 정확도={m_eval3[1]:.4f}')

print('4) model subclassing 사용(완전 자유로운 형태 - 프로그램 능력 중요)')
class MyModel(Model):
    def __init__(self):
        super(MyModel, self).__init__()
        self.dense1 = Dense(units=4, activation='relu')
        self.dense2 = Dense(units=1, activation='sigmoid')
    
    def call(self, inputs):
        x = self.dense1(inputs)
        return self.dense2(x)
    
sub_model = MyModel()

sub_model.build(input_shape=(None, 2))
print(sub_model.summary())

sub_model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.01), metrics=['accuracy'])
sub_model.fit(x_data, y_data, epochs=20, batch_size=1, verbose=0)
m_eval_sub = sub_model.evaluate(x_data, y_data)
print(m_eval_sub)
print(f'평가 결과_sub : 손실={m_eval_sub[0]:.4f}, 정확도={m_eval_sub[1]:.4f}')




