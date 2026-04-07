# logisticregresion(로지스틱 회귀분석)
# 선형결합을 로그오즈(logit())로 해석하고 이를 시그모이드 함수를 통해 확률로 변환
# 이항 분류(다항도 가능), 독립변수:연속형 종속변수:범주형
# logisticRegresion을 근거로 뉴럴넷의 뉴런 에서 사용

# mtcars dataset 사용
import numpy as np
import statsmodels.api as sm

mtcarsdatas = sm.datasets.get_rdataset("mtcars")
print(mtcarsdatas.keys())
mtcars = sm.datasets.get_rdataset("mtcars").data
print(mtcars.head(2))
print(mtcars.info())

# 연비와 마력수에 따른 변속기 분류
mtcars = mtcars.loc[:, ['mpg', 'hp', 'am']]
print(mtcars.head(2))
print(mtcars['am'].unique())

# 모델 작성 방법1 : logit()
import statsmodels.formula.api as smf
formula = 'am ~ hp + mpg'  # 연속형 ~ 범주형 + ....
result = smf.logit(formula=formula, data=mtcars).fit()
print(result.summary())  # logit regression results

# print("예측값 : ", result.predict(mtcars))
pred = result.predict(mtcars[:10])
print('예측값 : ', pred.values)
print('예측값 : ', np.around(pred.values))
print('실제값 : ', mtcars['am'][:10].values)
print()
print('수치에 대한 집계표(confusion matrix, 혼돈행렬) 확인---')
conf_tab =result.pred_table()
print(conf_tab)

# 현재 모델의 분류 정확도 확인 1 - confusion matrix 사용
print('분류 정확도 : ', (16 + 10) / len(mtcars))
print('분류 정확도 : ', (conf_tab[0,0] + conf_tab[1,1]) / len(mtcars))

# 모듈로 확인 2 - accuracy_score 사용
from sklearn.metrics import accuracy_score
pred2 = result.predict(mtcars)
print('분류 정확도 : ', accuracy_score(mtcars['am'], np.around(pred2.values)))

print('*'*50)

# 모델 작성 방법2 : glm() 사용 일반화된 선형 모델
# Binomial() : 이항분포, Gaussian() : 정규분포 - 기본값
result2 = smf.glm(formula=formula, data=mtcars, family=sm.families.Binomial()).fit()
print(result2.summary())

glm_pred = result2.predict(mtcars[:10])
print('glm 예측값 : ', np.around(glm_pred.values))
print('실제값 : ', mtcars['am'][:10].values)

glm_gred2 = result2.predict(mtcars)
print('glm 모델 분류 정확도:', accuracy_score(mtcars['am'], np.around(glm_gred2.values)))

# logit()은 변환 함수, glm()은 logit을 포함한 전체 모델
import pandas as pd 
print('새로운 값으로 분류 ---------')
newdf = pd.DataFrame()
newdf['hp'] = [100, 110, 80, 130]
newdf['mpg'] = [10, 30, 120, 200]
print(newdf)

new_pred = result.predict(newdf)
print('새로운 값 예측 : ', np.around(new_pred.values))
print('새로운 값 예측 : ', np.rint(new_pred.values))