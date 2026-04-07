# 선형회귀분석의 모형의 적절성 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
import statsmodels.formula.api as snf

df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/Carseats.csv" )
print(df.head(3), df.shape)
print(df.info())
df = df.drop([df.columns[6],df.columns[9],df.columns[10]], axis=1)
print(df.corr())
lm = snf.ols(formula="Sales ~ Income+Advertising+Price+Age", data=df).fit()
print(lm.summary())

print("\n선형회귀 모델의 적절성 조건 체크 후 모델 사용")
print(df.columns)
df_lm = df.iloc[:, ]
# 잔차항 구하기
fitted = lm.predict(df)

# 유의한 모델이므로 생성된 
# 방법1 
# import pickle
# with open("carseat.pickle", "wb") as obj:  # 저장
#     pickle.dump(lm, obj)

# with open("carseat.pickle", "rb") as obj: # 읽기
#     mymodel = pickle.load(lm, obj)
# 방법2 : pickle은 binary로 i/o해야하므로 번거롭다
import joblib
joblib.dump(lm, "carseat.model")
# 이후 부터는 아래 처럼 읽어 사용하면 됨 
mymodel = joblib.load("carseat.model")