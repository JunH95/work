import pandas as pd
import numpy as np


# 1. 파일 읽기 (판다스가 첫 줄을 제목으로 알아서 읽도록 둡니다)
url = 'https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/titanic_data.csv'
df = pd.read_csv(url)

# 2. 전처리: 컬럼명 공백 제거 
df.columns = df.columns.str.strip()

# 4. 나이대 구간 설정
bins = [1, 20, 35, 60, 150]
labels = ["소년", "청년", "장년", "노년"]
df["agegroup"] = pd.cut(df["Age"], bins=bins, labels=labels)

# --- 1) 나이대별 생존자 수 ---
# observed=False는 카테고리형 데이터 경고를 없애줍니다.
count = df.groupby("agegroup", observed=False)["Survived"].sum()
print(count)

# --- 2) 성별/선실별 생존율 (샘플1 형태) ---
pivot1 = df.pivot_table(index='Sex', columns='Pclass', values='Survived', aggfunc='mean', observed=False)
print(pivot1)


# --- 3) 성별/나이대/선실별 생존율 (샘플2 형태: 백분율) ---
pivot2 = df.pivot_table(index=['Sex', 'agegroup'], columns='Pclass', values='Survived', aggfunc='mean', observed=False)
pivot2_percent = (pivot2 * 100).round(2)
print(pivot2_percent)

# 1)
df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/human.csv",skipinitialspace=True)
print(df)
df.columns = df.columns.str.strip()
print(df.dropna(subset=["Group"]))
df1 = df.dropna(subset=["Group"])
print(df1[['Career', 'Score']])
print(df1[['Career', 'Score']].mean())

# 2)
df3 = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/tips.csv")
print(df3.info())
print(df3.head(3))
print(df3.describe())
print(df3["smoker"].value_counts())
print(df3["day"].unique())