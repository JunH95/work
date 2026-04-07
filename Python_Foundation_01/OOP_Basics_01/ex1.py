var1 = "안녕 파이썬"
print(var1)

# 한 줄 주석

"""
여러줄 
주석

"""

var1 = 5;
var1 = 10
print(var1)

# 파이썬은 모든 변수가 참조형 -> 기억 장소의 주소를 기억, 타입을 선언X, 
# ; 한줄에 명령문 구분할 때 사용 추천 X

# ctrl + ` 터미널과 이동

var1 = 5.6
print(var1)

var2 = var1 # 두 변수가 같은 객체의 주소값을 가짐
print(var1, var2)

var3 = 7
print(var1, var2, var3)

print(id(var1), id(var2), id(var3)) # id() 각 변수의 주소를 확인 

Var3 = 8
print(var3, Var3) # 대소문자 구분,  영어로 시작, 숫자로 시작X, 특수문자 사용X

a = 5
b = a
c = 5
print(a, b, c)
print(a is b, a == b) # is 주소 비교 연산, == 값 비교 연산
print(b is c, b == c)

aa = [5]
bb = [5]
print(aa, bb)
print(aa is bb, aa == bb) # 주소는 False 값은 True, 집합형 변수의 경우 주소가 다름

print("-------")  # " ", ' ' 상관 없음 구분X
import keyword # 키워드 목록 확인용 모듈 읽기
print("예약어 목록:", keyword.kwlist) # 키워드는 변수명, 함수명, 클래스명 등 으로 사용 불가

# for = 4 오류 발생 for은 예약어

print("type(자료형) 확인")
kbs = 9
print(isinstance(kbs, int))
print(isinstance(kbs, float))
print(5, type(5)) # 5 <class 'int'> 클래스 는 객체(object) 의 타입이 int 정수 이다
print(5.1, type(5.1)) # 5.1 <class 'float'> 객체의 타입은 float 실수
print(3+4j, type(3+4j)) # (3+4j) <class 'complex'> complex 복소수
print(True, type(True)) # True <class 'bool'> bool 참 거짓
print("good", type("good")) # good <class 'str'> str 문자형

# 묶음형 자료 
print((1,), type((1,))) # (1,) <class 'tuple'> 
print([1], type([1])) # [1] <class 'list'>
print({1}, type({1})) # {1} <class 'set'>
print({"k":1}, type({"k":1})) # {'k': 1} <class 'dict'> key와 value를 : 으로 구분



