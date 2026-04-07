
# [문항1] 집합형 자료를 이용해 리스트 타입의 li 변수가 기억하고 있는 값의 중복을 제거한 후 계속해서 리스트 타입의 값을 유지하려고 한다.
# 자료구조의 형식을 변경하는 함수를 이용하려고 할 때, 아래의 빈 칸을 순서대로 채우시오. (배점:5)
# li = [1, 2, 2, 2, 3, 4, 5, 5, 5, 2, 2]
# im = set(li)
# li = list(im)
# print(li)

# for i in {1, 2, 3, 4, 5, 5, 5, 5}:
#     print(i, end = ' ')


	
# [문항3] 반복문 for를 사용 : 1 ~ 100 사이의 숫자 중 3의 배수 또는 4의 배수 이고 7의 배수가 아닌 수를 출력하고 건수와 합도 출력하는 코드를 작성하시오
# 출력 결과
# 3 4 6 8 9 12 15 16 18 20 21 24 27 30 ...
# 건수 : ...
# 배수의 총합 : ...
# (배점:5)

# count = 0
# total = 0
# for i in range(1, 101):
#     if (i % 3 == 0 or i % 4 == 0) and i % 7 != 0:
#         print(i, end=" ")
#     count += 1
#     total += i

# print("\n건수 : ", count)
# print("배수의 총합 : ", total)

# print(5 / 3)
# print(5 // 3)
# print(5 % 3)


# *v1, v2, v3 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
# print(v1)
# print(v2)
# print(v3)

# print(list(range(1, 6, 2)))



# aa = int(input())
# bb = 10 / aa
# try:
#     print(bb)

# except ZeroDivisionError:
#     print("0으로는 나눌 수 없습니다")


# [문항11] tom은 그림과 같은 모양의 *(별 문자)을 출력하고 싶어 한다.
# while문을 사용하여 tom이 원하는 별 모양을 출력하는 코드를 작성하시오.

# i = 1
# while i <= 10:
#     print("*" * (11 - i))
#     i += 1


# tom과 james는 커피를 마시며 윤년에 대한 대화를 나누고 있었다.
# tom에 의하면 '윤년은 과년'이라고도 하며, 역법인 태음력이나 태양력에서, 
# 자연의 흐름에 대해서 생길 수 있는 오차를 보정하기 위해 삽입하는 날이나 주, 달이 들어가는 해를 말하는데, 
# 윤년인 해에는 2월달이 29일이 된다고 한다.
# 이런 얘기를 듣던 james가 노트북을 켜더니 파이썬의 if문을 이용하여 프로그램을 작성했다. 
# james가 키보드를 이용하여, 연도를 입력해 실행한 결과는 아래와 같다. james가 작성한 코드를 적어 보시오.

# 처리 조건 : 특정 년도는 4의 배수이고 100의 배수가 아니거나 400의 배수이면 윤년이다.

# 실행 2회 실행 예)
# 연도 입력:2020
# 2020년은 윤년
# 연도 입력:2022
# 2020년은 평년 (배점:10)

# year = int(input())
# print("연도 입력:", year)

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f"{year}은 윤년")
# else:
#     print(f"{year}은 평년")


	
# [문항13] while 문을 사용 : 1 ~ 100 사이의 정수 중에서 3으로 끝나는 숫자만 출력하는 코드를 작성 하시오.

# 출력 결과는 아래와 같다.
# 3 13 23 33 43 53 63 73 83 93 (배점:10)
# 아래 소스 코드의 빈 칸을 차례대로 채우시오.
# i = 0
# while True:
#     if 1)__________:
#         i += 1
#         2)_________       
             
#     if i > 100: 3)________
               
#     print(i, end=' ')
#     4)________

# i = 0
# while True:
#     if i % 10 != 3:
#         i += 1
#         continue
#     if i > 100:
#         break
#     print(i, end=" ")
#     i += 1

# [문항14] while 반복문을 사용하여 아래와 같이 3, 5, 7, 9 단의 구구단을 출력하는 코드를 작성하시오.
# (배점:10)
# 출력결과 :
# 3*1=3 3*2=6 3*3=9 3*4=12 3*5=15 3*6=18 3*7=21 3*8=24 3*9=27
# 5*1=5 5*2=10 5*3=15 5*4=20 5*5=25 5*6=30 5*7=35 5*8=40 5*9=45
# 7*1=7 7*2=14 7*3=21 7*4=28 7*5=35 7*6=42 7*7=49 7*8=56 7*9=63
# 9*1=9 9*2=18 9*3=27 9*4=36 9*5=45 9*6=54 9*7=63 9*8=72 9*9=81

# i = 3
# while i < 10:
#     j = 1
#     while j < 10:
#         j += 1
#         print("{}*{}={}".format(i, j, i*j), end=" ")
#     print()
#     i += 2

	
# [문항15] 아래 코드가 동작하도록 자전거 클래스(Bicycle class)를 정의하시오.

# 조건1 : 멤버 변수는 name, wheel, price 이다.
# 조건2 : 바퀴 가격은 바퀴수 * 가격이다.

# 실행 및 출력 결과)
# gildong = Bicycle('길동', 2, 50000) # 생성자로 name, wheel, price 입력됨
# gildong.display()

# 길동님 자전거 바퀴 가격 총액은 100000원 입니다. (배점:10)

# class Bicycle:
#     def __init__(self, name, wheel, price):
#         self.name = name
#         self.wheel = wheel
#         self.price = wheel * price
    
#     def display(self):
#         print(f"{self.name} 자전거 바퀴의 총액은 {self.price}원 입니다.")


# gildong = Bicycle('길동', 2, 50000)
# gildong.display()

	
# [문항8] 아래의 코드를 람다 함수를 이용한 소스 코드로 적으시오. (배점:5)
# def Hap(m, n):
#   return m + n * 5

# print("\n축약함수(lambda function) : 이름이 없는 한 줄짜리 함수")
# # 형식 : lambda 매개변수들,,,:반환식            <== return 없이 결과 반환
# def hapFunc(x, y):
#     return x + y
# print(hapFunc(1, 2))
# # 람다로 표현
# print((lambda x, y:x + y)(1, 2))

# gg = lambda x, y:x + y
# print(gg(1,2))

# lambda x, y:x + y * 5


# [문항7] 1) 아래와 같은 명령문을 수행한 후의 결과를 적으시오.

# 2) '*' 연산자의 기능도 간단히 적으시오.

# *v1, v2, v3 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
# print(v1)
# print(v2)
# print(v3)
# (배점:5)


# [문항6] 아래 Mbc 함수에서 c 는 전역, b는 Kbs 함수의 b를 취하려고 한다.
# 빈 칸에 알맞은 키워드를 차례대로 적으시오. (배점:5)
# a = 1.5; b = 2; c = 3
# def Kbs():
#     a = 20
#     b = 30
#     def Mbc():
#         global c
#         nonlocal b
#         print("Mbc 내의 a:{}, b:{}, c:{}".format(a, b, c))
#         c = 40
#         b = 50
#     Mbc()
# Kbs()