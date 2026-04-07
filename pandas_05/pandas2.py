# 재색인
from pandas import Series, DataFrame
import numpy as np

# Series의 재색인
data = Series([1, 3, 2], index=(1,4,2))
data2 = data.reindex((1,2,4))

# 재색인 할때 값 채워 넣기
data3 = data2.reindex([0,1,2,3,4,5], fill_value=777)
print(data3)

# NaN을 앞 값으로 NaN을 채움
data3 = data2.reindex([0,1,2,3,4,5], method="ffill")
print(data3)
data3 = data2.reindex([0,1,2,3,4,5], method="pad")
print(data3)

# NaN을 다음 값으로 NaN을 채움
data3 = data2.reindex([0,1,2,3,4,5], method="bfill")
print(data3)
data3 = data2.reindex([0,1,2,3,4,5], method="backfill")
print(data3)

# DataFrame bool 처리
df = DataFrame(np.arange(12).reshape(4,3), index=["1월","2월","3월","4월",],
            columns=["강남","강북","서초",])
            
print(df)
print(df["강남"])
print(df["강남"] > 3)
print(df[df["강남"] > 3])

print(df < 3)
df[df < 3] = 0
print(df)

# 슬라이싱 관련 메소드 : loc():라벨지원, iloc():숫자지원
print(df.loc["3월", :])
print(df.loc[:"2월"])
print(df.loc[:"2월", ["서초"]])

print(df.iloc[2])
print(df.iloc[2, :])
print(df.iloc[:3])
print(df.iloc[:3, 2])
print(df.iloc[:3, 1:3])