# [로지스틱 분류분석 문제1]
# 문1] 소득 수준에 따른 외식 성향을 나타내고 있다. 주말 저녁에 외식을 하면 1, 외식을 하지 않으면 0으로 처리되었다. 
# 다음 데이터에 대하여 소득 수준이 외식에 영향을 미치는지 로지스틱 회귀분석을 실시하라.
# 키보드로 소득 수준(양의 정수)을 입력하면 외식 여부 분류 결과 출력하라.
# 요일,외식유무,소득수준
# 토,0,57
# 토,0,39
# 토,0,28
# 화,1,60
# 토,0,31
# 월,1,42
# 토,1,54
# 토,1,65
# 토,0,45
# 토,0,37
# 토,1,98
# 토,1,60
# 토,0,41
# 토,1,52
# 일,1,75
# 월,1,45
# 화,0,46
# 수,0,39
# 목,1,70
# 금,1,44
# 토,1,74
# 토,1,65
# 토,0,46
# 토,0,39
# 일,1,60
# 토,1,44
# 일,0,30
# 토,0,34

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

data = {
    '요일': ['토', '토', '토', '화', '토', '월', '토', '토', '토', '토', '토', '토', '토', '토', '일', '월', '화', '수', '목', '금', '토', '토', '토', '토', '일', '토', '일', '토'],
    '외식유무': [0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    '소득수준': [57, 39, 28, 60, 31, 42, 54, 65, 45, 37, 98, 60, 41, 52, 75, 45, 46, 39, 70, 44, 74, 65, 46, 39, 60, 44, 30, 34]
}

df = pd.DataFrame(data)
print("전체 데이터 상위 5개 확인:")
print(df.head())

# 1. 문제 조건 분석: '주말 저녁'에 해당하는 주말 데이터만 추출 (토, 일)
df = df[df['요일'].isin(['토', '일'])]
print("\n주말 데이터만 필터링한 결과:")
print(df) 

# 2. 로지스틱 회귀 모델 학습 (두 가지 방법 모두 사용)
# 방법 1: logit() 함수 사용
model1 = smf.logit('외식유무 ~ 소득수준', data=df).fit()
# 방법 2: glm() 함수 사용 (선형 모델 중 이항분포 지정)
model2 = smf.glm('외식유무 ~ 소득수준', data=df, family=sm.families.Binomial()).fit()

# 3. 사용자로부터 예측할 임의의 소득 수준 하나(정수) 입력받기
input_income = int(input("\n소득 수준을 입력하세요 : "))

# 4. 입력받은 소득 수준을 모델 예측에 넣기 위해 DataFrame 형태로 변환
newdf = pd.DataFrame()
newdf['소득수준'] = [input_income] 

# 5. 모델을 사용하여 입력한 소득에 대한 예측값(확률) 가져오기
pred1 = model1.predict(newdf)
pred2 = model2.predict(newdf)

# np.around()를 사용하여 확률(0~1)을 0 또는 1로 반올림 처리
print("\n--- 예측 결과 (내부 확률값 기준) ---")
print('model1(logit) 예측값 :', np.around(pred1.values))
print('model2(glm) 예측값 :', np.around(pred2.values))

# 6. 예측 결과 해석 및 사용자에게 친절하게 출력하기
print("\n--- 최종 분류 결과 출력 ---")
# 예측값이 1이면 외식 함, 아니면 외식 안 함으로 출력 (삼항 연산자)
print('model1 분류 결과: 외식 함 ' if np.around(pred1.values[0]) == 1 else 'model1 분류 결과: 외식 안함 ')
print('model2 분류 결과: 외식 함 ' if np.around(pred2.values[0]) == 1 else 'model2 분류 결과: 외식 안함 ')

# 7. 현재 만들어진 모델들의 분류 정확도(Accuracy) 채점하기
from sklearn.metrics import accuracy_score
print("\n--- 모델 정확도(평가) ---")

# 주말 전체 데이터(df)를 넣고 예측시킨 후 실제 정답(df['외식유무'])과 비교
pred_all1 = model1.predict(df)
print('model1 분류 정확도 :', accuracy_score(df['외식유무'], np.around(pred_all1.values)))

pred_all2 = model2.predict(df)
print('model2 분류 정확도 :', accuracy_score(df['외식유무'], np.around(pred_all2.values)))