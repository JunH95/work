# 연산자

v1 = 3    # 치환 연산자
v1 = v2 = v3 = 5
print(v1, v2, v3)

print("출력1")
print("출력2") # print문 자동 라인스킵

print("출력1", end =",")
print("출력2")
print("출력3")

print("출력1", end =" ")
print("출력2")
print("출력3")


v1, v2 = 10, 20
print(v1, v2)
v2, v1 = v1, v2
print(v1, v2)

print("값 할당 : packing 연산")
v1 = 1,2,3,4,5  # v1 = (1,2,3,4,5) 같음 group
v1 = [1,2,3,4,5]

# v1, v2 = [1,2,3,4,5] Error
*v1, v2 = [1,2,3,4,5] 
print(v1, " ", v2)

# v1, v2* = [1,2,3,4,5] SyntaxError: invalid syntax  
*v1, v2, v3 = [1,2,3,4,5]
print(v1, " ", v2, " ", v3)

print(format(1.5678, '10.3f')) # 전체 10자리 중 소수 이하 4번째에서 반올림
print('나는 나이가 %d 이다.'%23) # %d -> 정수
print('나는 나이가 %s 이다.'%'스물셋') # %s -> 문자
print('나는 나이가 %d 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 나이가 %s 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 키가 %f이고, 에너지가 %d%%.'%(177.7, 100)) # %f 실수

print('이름은 {0}, 나이는 {1}'.format('한국인', 33))
print('이름은 {}, 나이는 {}'.format('신선해', 33))
print('이름은 {1}, 나이는 {0}'.format(34, '강나루'))

abc = 123
print(f"abc의 값은 {abc}임")
print()
print("\n본격적 연산 -------------") # \n(줄바꿈), \b(백스페이스), \t(탭) .... escape 문자 

print(5 + 3, 5 - 3, 5 * 3, 5 / 3, 5 // 3, 5 % 3, 3 ** 3)
#       8      2      15  1.6666666666666667 1(몫) 2(나머지) 27

print(divmod(5, 3), " ", 5 % 3)

result = 3 + 4 * 5 + (2 + 3) / 2 # 연산자 우선 순위 () -> ** -> 단항 -> 산술(* / // %) -> 산술(+ -) -> 관계 -> 논리(not -> and -> or) -> 치환
print(result) 

print(5 > 3, 5 == 3, 5 != 3) 
print(5 > 3 and 4 < 3, 5 > 3 or 4 < 3, not(5 >= 3))
print(True or False and False) # True
print(True and False or False) # False 

print(4 + 5) # 산술연산
print("4" + "5") # 문자열 덧셈

print("한" + "국" + "만세")
print("한국" * 5)


# 누적
print("누적")
a = 10
a += 1 # a = a + 1 같음(처리 속도가 느림) , -= *= /= 있음, 
print(f"a는 {a}")

# print(a++)  --  ++ 증감 연산자 파이썬 없음

print(--a) # 증감 연산자 아님 부호 연산
print(-a)
print(a * -1)

print(1 + 1)
# print(("1" + "1") + 1) TypeError 문자 숫자 연산 에러
print(int("1" + "1") + 1) # 문자열을 int(정수) 로 형 변환 
print(float("1" + "1") + 1) # float 실수화
# print(float(1 + 1) + "1") TypeError 문자 숫자 연산 에러
print(str(1 + 1) + "1") # str 문자화

print("boolean 처리 :", bool(True), bool(False))
print(bool(1), bool(12.3), bool("ok"), bool([12])) # data 있으면 True
print(bool(0), bool(0.0), bool(" "), bool([ ]), bool(None)) # 값이 없으면 False

# r 선행문자

print("aa\tbb") 
print("aa\nbb")

print(r"aa\tbb") # r은 escape 문자 무시할 때 
print(r"aa\tbb")

