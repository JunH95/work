# 고수준의 자료구조(Series, DataFrame)와 빠르고 쉬운 데이터 분석용 함수 제공
# 통합된 시계열 연산, 축약연산, 누락 데이터 처리, SQL, 시각화 등 제공
# 데이터 랭글링(Data Wrangling), 데이터 먼징(Data Munging)을 효율적으로 처리 가능

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# Series : 일련의 객체를 담을 수 있는 1차원 배열과 같은 자료구조로 색인(index)를 갖는다
obj = pd.Series([3, 7, -5, 4])
# obj = pd.Series([3, 7, -5, "4"])   # 요소값은 object type 뭐든지 들어갈 수 있음
# obj = pd.Series((3, 7, -5, 4))
# obj = pd.Series({3, 7, -5, 4}) TypeError : set type is unordered
print(obj)

obj2 = pd.Series([3, 7, -5, 4], index=["a","b","c","d"])
print(obj2)
print(obj2.sum(), " ", np.sum(obj2), " ", sum(obj2))
print(obj2.std())

print(obj2.values)
print(obj2.index)
print(obj2["a"])   # 3
print(obj2[["a"]]) # a 3
print(obj2[["a", "b"]])
print(obj2["a":"C"])
print(obj2[2])   # 인덱스 사용 
print(obj2.iloc[2])
print(obj2[1:4])

print(obj2[[2, 1]])
print(obj2.iloc[[2,1]])

print("a" in obj2)
print("k" in obj2)

# 파이썬 dict 자료를 Series 객체로 생성
names = {"mouse":5000, "keyboard":25000, "monitor":450000}
obj3 = Series(names)
print(obj3)
obj3.index = ["마우스", "키보드", "모니터"]
print(obj3)
obj3.name = "상품가격"
print(obj3)

# DataFrame 객체
df = pd.DataFrame(obj3)
print(df)

data = {
    "irum" : ["홍길동","한국인","신기해","공기밥","한가해"],
    "juso" : ("역삼동","신당동","역삼동","역삼동","신사동"),
    "nai" : [23,25,33,231,35]
}

frame = pd.DataFrame(data)
print(frame)

print()
print(frame["irum"])
# print(frame.irum) Series
# Series가 모여 DataFrame

print(DataFrame(data=data, columns=["juso", "irum", "nai"])) # column 순서 변경 가능

# NaN (결측치)
frame2 = pd.DataFrame(data, columns=["irum", "nai", "juso", "tel"],
                    index=["a","b","c","d","e"]
                    )
print(frame2)

frame2["tel"] = "111-1111"  # 모든 행 적용 
print(frame2)

val = pd.Series(["222-2222", "333-3333", "444-4444"], index=["b","c","e"])  # Series는 DataFrame의 하나의 열로 취급
print(val)
frame2["tel"] = val  # 덮어쓰기
print(frame2)
print()

print(frame2.T)   # 전치(행과 열이 바뀜)

print(frame2.values) # 결과는 list type
print(frame2.values[0,1])  # 인덱싱/슬라이싱 가능
print(frame2.values[0:2])

# 행삭제
frame3 = frame2.drop("d")
# frame3 = frame2.drop("d", axis=0) 같은 의미
print(frame3)

#열삭제
frame4 = frame2.drop("tel", axis=1)
print(frame4)

# 행단위 정렬
print(frame2.sort_index(axis=0, ascending=False))
# 열단위 정렬
print(frame2.sort_index(axis=1, ascending=True))

# 사전 순서로 순위
print(frame2.rank(axis=0))

counts = frame2["juso"].value_counts()
print(counts)

# 문자열 자르기
data = {
    "juso" : ["강남구 역삼동", "중구 신당동", "강남구 대치동"],
    "inwon" : [23, 25, 15]
}

fr = pd.DataFrame(data)
print(fr)

result1 = Series([x.split()[0] for x in fr.juso])
result2 = Series([x.split()[1] for x in fr.juso])
print(result1)
print(result2)