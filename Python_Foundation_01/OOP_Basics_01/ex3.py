# 기본 자료형 : int, float, bool, complex

# 묶음 자료형 : str, list, tuple, set, dict

# 1) str : 문자열 묶음 자료형, 순서 O, 수정 X 
s = "sequence"
print(s, id(s)) # 가장 첫번째 것(s)의 주소만 기억
print("길이 : ", len(s))
print(s[0], s[2])
print("길이 : ", s.find("e"), s.find("e", 3), s.rfind("e")) # 문자열 관련 함수

# 인덱싱 / 슬라이싱
#   순서가 있을 때만 가능

print(s[5]) # 인덱싱  변수명[순서], 순서를 index라고 함, index는 0부터 출발
print(s[2:5]) # 슬라이싱 2 이상 5 미만, 변수[start:end:간격]
print(s[:]) 
print(s[:], " ", s[0:len(s)], " ", s[::1]) 
print(s[0:7:2]) 
print(s[-1], " ", s[-4:-1:1]) # - 는 뒤에서부터 

print(s, id(s))  # 수정 X 변경 O 새로운 값으로 대체(주소가 변경되었음)
s = "sequenc"
print(s, id(s))
s = "bequence"
print(s, id(s))

print("-----" * 10)

# 2) List : 다양한 종류의 자료 묶음형, 순서 O, 수정 O, 중복 O
a = [1, 2, 3]
print(a, a[0], a[0:2])
b = [10, a, 10, 20.5, True, "문자열"] # list 안에 list, str bool int float 전부 들어갈 수 있음, 첫 10 과 세번째 10 주소 같음 
print(b, " ", b[1], " ", b[1][0]) # b 1번째인 a의 0번째
print()
family = ["엄마", "아빠", "나", "여동생"] # 수정 가능(주소가 변경되지 않음), 
print(id(family))
family.append("남동생") # append 리스트에 추가
family.remove("나") # 삭제
family.insert(0, "할머니") # 삽입 원하는 위치
family.extend(["삼촌", "고모", "조카"]) # 추가
family += ["이모"] # 추가
print(id(family))
print(family)
print(family.index("아빠")) # list 안에서 아빠 index의 위치를 표현
print("엄마" in family, "나" in family) # 있으면 True, 없으면 False

family.remove("아빠") # 값에 의한 삭제

del family[2] # 순서에 의한 삭제
print(family)

print()

kbs = ["123", "34", "234"]
kbs.sort()   # 문자열 정렬
print(kbs) 

mbc = [123, 34, 234]
mbc.sort()    # 숫자 정렬(ascending sort, 오름차순)
mbc.sort(reverse=True)    # 숫자 정렬(decending sort, 내림차순)
print(mbc)

sbs = [123, 34, 234]
ytn = sorted(sbs)
print(sbs)
print(ytn)

print()

name = ["tom", "james", "oscar"]
name2 = name   # 주소 자체를 치환
print(name, id(name))
print(name2, id(name2))


import copy
name3 = copy.deepcopy(name) # 새로운 객체에게 값을 치환
print(name3, id(name3))

name[0] = "길동"  # name3에는 영향이 없다 새로운 객체이기 때문
print(name)
print(name2)
print(name3)

# 3) tuple : list와 유사, 읽기 전용(수정 불가), 순서 O, 중복 O

t = (1, 2, 3, 4)
# t = 1, 2, 3, 4 위와 동일
print(t, type(t))

# k = (1) # 이때 k 는 int
k = (1,) # 이때 k 는 tuple
print(k, type(k)) 

print(t[0], " ", t[0:2])
# t[0] = 77 수정 불가 TypeError: 'tuple' object does not support item assignment

imsi = list(t)  # tuple은 수정불가하니 list로 변경하여 수정 후 다시 tuple로 변경
imsi[0] = 77
t = tuple(imsi)
print(t)

# 4) set : 순서 X, 중복 X 수정 가능

ss = {1, 2, 1, 3}
print(ss) # 중복 값은 제거
ss2 = {3, 4}

print(ss.union(ss2))   # 합집합
print(ss.intersection(ss2))   # 교집합
print(ss - ss2, ss | ss2, ss & ss2)   # 차집합, 합집합, 교집합
# print(ss[0]) # TypeError: 'set' object is not subscriptable 순서가 없기 때문에 인덱싱 / 슬라이싱 불가
ss.update({6, 7})
print(ss)
ss.discard(7) # 값 삭제 : 해당 값 없으면 통과
ss.discard(7) # 값 삭제 있으면 지우고 없으면 스킵
ss.remove(6) # 값 삭제 : 해당 값 없으면 에러
# ss.remove(6) # 값 삭제 있으면 지우고 없으면 Error

print(ss)

li = ["aa", "aa", "bb", "cc", "aa"] # list에서 중복 값을 제거하고 싶을때 set으로 한번 바꿨다 다시 list로 바꿈
print(li)
imsi = set(li)
li = list(imsi)
print(li)


# 5) dict : 사전 자료형 {"키":값} 형태, 순서X, 수정 O

# 방법 1 dict함수를 이용
mydic = dict(k1 = 1, k2 = "ok", k3 = 123.4)
print(mydic, type(mydic))

# 방법 2 
dic = {"파이썬":"뱀", "자바":"커피", "인사":"안녕"}
print(dic)
print(len(dic))
print(dic["자바"]) # 키를 통해 값을 찾음
ff = dic.get("자바")
print(ff)

# print(dic["커피"]) 
# print(dic[0]) 인덱싱 / 슬라이싱 불가
dic["금요일"] = "와우"  # 추가
print(dic)

del dic["인사"]
print(dic)
print(dic.keys())  # 키 목록
print(dic.values())  # 값 목록
