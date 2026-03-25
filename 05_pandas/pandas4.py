# DataFrame 재구조화(열을 행으로 , 행을 열로 이동)

import pandas as pd
import numpy as np

df = pd.DataFrame(1000 + np.arange(6).reshape(2,3), index=["대전", "서울"], columns=["2020","2021","2022"])
print(df)

# stack unstack
df_row = df.stack()  # 열을 행으로 변경
print(df_row)

df_col = df_row.unstack()  # 행을 열로 이동
print(df_col)

# 범주화
price = [10.3, 5.5, 7.8, 3.6]
cut = [3, 7, 9, 10]  # 구간 기준값
result_cut = pd.cut(price, cut)  # 연속형 데이터를 범주화
print(result_cut) #  [(3, 7] < (7, 9] < (9, 10]]  () 초과미만 [] 이상이하
print(pd.Series(result_cut).value_counts())
print()

datas = pd.Series(np.arange(1, 1001))
print(datas.head())  #  앞 5개
print(datas.tail())  #  뒤 5개

result_cut2 = pd.qcut(datas, 3)
print(result_cut2)
print(pd.Series(result_cut2).value_counts())

# agg함수 :범주의 그룹별 연산
group_col = datas.groupby(result_cut2, observed=True)
print(group_col.agg(["count", "mean", "std", "min"]))

# agg 대신 사용자 함수를 작성
def summaryFunc(gr):
    return {"count":gr.count(),
            "mean":gr.mean(),
            "std":gr.std(),
            "min":gr.min(),
            }
print(group_col.apply(summaryFunc))
print(group_col.apply(summaryFunc).unstack())

# merge : DataFrame 객체 병합
df1 = pd.DataFrame({"data1":range(7), "key":["b","b","a","c","a","a","b"]})
df2 = pd.DataFrame({"key":["a","b","d"],"data2":range(3)})
print(df1)
print(df2)
print(pd.merge(df1, df2, on="key"))  # key를 기준으로 병합 교집합 inner join
print(pd.merge(df1, df2, on="key", how="inner")) 

print(pd.merge(df1, df2, on="key", how="outer")) 
print(pd.merge(df1, df2, on="key", how="left"))
print(pd.merge(df1, df2, on="key", how="right"))  


# 공통 컬럼명이 없는 경우 
df3 = pd.DataFrame({"key2":["a","b","d"], "data2":range(3)})
print(pd.merge(df1, df3, left_on="key", right_on="key2"))  # inner join

# concat
print(pd.concat([df1, df3], axis=0))  # 행단위 
print(pd.concat([df1, df3], axis=1))  # 열단위 

# pivot_table : pivot 과 groupby 명령의 중간적 성격
# pivot : 데이터 열 중에서 두개의 열(key)을 사용해 데이터의 행열을 재구성

data = {"city":["강남","강북","강남","강북"],
        "year":[2000, 2001, 2002, 2002],
        "pop":[3.3, 2.5, 3.0, 2.0]}
df = pd.DataFrame(data)
print(df)
print(df.pivot(index="city",columns="year",values="pop"))
print(df.pivot(index="year",columns="city",values="pop"))

# set_index : 기존 행 인덱스를 제거하고 첫번째 열 인덱스 설정
print(df.set_index(["city", "year"]).unstack())

print(df["pop"].describe())
print(df.pivot_table(index=["city"]))
print(df.pivot_table(index=["city"], aggfunc='mean'))
print(df.pivot_table(index=["city", "year"], aggfunc=[len, 'sum']))
print(df.pivot_table(values="pop", index="city"))
print(df.pivot_table(values="pop", index="city", aggfunc=len))

print(df.pivot_table(values="pop", index="year", columns="city"))
print(df.pivot_table(values="pop", index="year", columns="city", margins=True))
print(df.pivot_table(values="pop", index="year", columns="city", margins=True, fill_value=0))

hap = df.groupby(["city"])
print(hap)
print(hap.sum())
print(df.groupby(["city"]).mean())