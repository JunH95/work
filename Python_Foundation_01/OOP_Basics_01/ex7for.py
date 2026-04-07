# 반복문 for

# for i in [1,2,3,4,5]: # 묶음형 자료가 있는동안 수행
#for i in (1,2,3,4,5):
for i in {1,2,3,4,5}:
    print(i, end = " ")

print("분산/표준편차-----")
# numbers = [1, 3, 5, 7, 9]
# numbers = [3,4,5,6,7]
numbers = [-3,4,5,7,12]

tot = 0
for a in numbers:
    tot += a
print(f"합은 {tot}, 평균은 {tot/len(numbers)}")
avg = tot / len(numbers)
# 편차의 합
hap = 0
for i in numbers:
    hap += (i - avg) ** 2 
print(f"편차제곱의 합 {hap}")
vari = hap / len(numbers)
print(f"분산은 {vari}")
print(f"표준편차 {vari ** 0.5}")

print()
colors = ["r", "g", "b"]
for v in colors:
    print(v, end = " ")

print("iter() : 반복 가능한 객체를 하나씩 꺼낼 수 있는 상태로 만들어주는 함수")
iterator = iter(colors)
for v in iterator:
    print(v, end = ", ")

print()
for idx, d in enumerate(colors): # 인덱스와 값을 반환
    print(idx, " ", d)

print("\n사전형-------")
datas = {"python":"만능어", "java":"웹용언어", "mariadb":"RDBMS"}
for i in datas.items():
    # print(i)
    print(i[0], " ~~ ", i[0])

for k, v in datas.items():
    print(k, " -- ", v)

for k in datas.keys():
    print(k, end = " ")
print()
for val in datas.values():
    print(val, end = " ")

print("다중 for문 ---------")
for n in [2,3]:
    print("--{}단--".format(n))
    for i in [1,2,3,4,5,6,7,8,9]:
        print("{} * {} = {}".format(n, i, n * i))

print("continue, break-------")
nums = [1,2,3,4,5]
for i in nums:
    if i == 2 :continue
    if i == 4 :break
    print(i, end= " ")
else:
    print("정상종료")

print("\n정규표현식 연습 + for")
str = """밀가루와 설탕, 전기 등 민생과 직결된 생필품 시장에서 수년간 짬짜미를 벌여 물가 상승을 초래한 혐의로 업체 관계자들이 무더기로 재판에 넘겨졌습니다.
서울중앙지검 공정거래조사부는 지난해 9월부터 생필품 담합 사건을 집중 수사한 결과, 시장 질서를 교란하고 서민 경제를 위협한 혐의로 업체 관계자 등 총 52명을 기소했다고 오늘(2일) 밝혔습니다."""

import re
str2 = re.sub(r"[^가-힣\s]", " ", str) # 한글과 공백 이외의 문자는 공백처리 str에서 ^ 대괄호 안에서 부정
print(str2)
str3 = str2.split((" ")) # 공백을 기준으로 문자를 분리
print(str3)
cou = {}
for i in str3:
    if i in cou:
        cou[i] += 1 # 같은 단어가 있으면 누적
    else:
        cou[i] = 1 # 최초의 단어인 경우는 "단어":1
print(cou)

print("정규 표현식 연습----------")
for test_ss in ["111-1234", "일이삼-일이삼사", "222-1234", "222&1234"]:
    if re.match(r"^\d{3}-\d{4}$", test_ss): # \d : 숫자 ^ : 시작 $ : 끝 대상은 test_ss
        print(test_ss, "전화번호 맞아요")
    else:
        print(test_ss, "전화번호 아니야")

print("comprehension : 반복문 + 조건문 + 값 생성을 한 줄로 표현")
a = [1,2,3,4,5,6,7,8,9,10]
li = []
for i in a:
    if i % 2 == 0:
        li.append(i)
print(li)

print(list( i for i in a if i % 2 == 0)) # 위 와 동일한 문장을 하나로 표현

# datas = [1, 2, "a", True, 3.0]
datas = {1, 2, "a", True, 3.0, 1, 2, 2, 1}

li2 = [ i * i for i in datas if type(i) == int ] 
print(li2)

id_name = {1:"tom", 2:"oscar"}
name_id = {val:key for key, val in id_name.items()}
print(name_id)

print()
print([1,2,3])
print(*[1,2,3]) # * : unpack
aa = [(1,2), (3,4), (5,6)]
for a, b in aa:
    print(a + b)

print([a + b for a, b in aa ], sep="\n")
print(*[a + b for a, b in aa ], sep="\n")

print("\n수열 생성 : range")
print(list(range(1, 6))) # [1, 2, 3, 4, 5]
print(list(range(1, 6, 1))) # 위랑 동일 증가치 생략하면 1 기본, 1부터 6미만 1씩 증가, 초기값 없으면 0부터 시작
print(tuple(range(1, 6, 2))) 
print(tuple(range(-10, -100, -20))) 
print(set(range(1, 6))) 
print()

for i in range(6):
    print(i, end= " ")

for _ in range(6):
    print("반복")

tot = 0
for i in range(1, 11):
    tot += i
print("tot : ", tot)
print("tot : ", sum(range(1, 11)))

for i in range(1, 10):
    print(f"2 * {i} = {2 * 1}")


# 문1 : 2~9 구구단 출력(단은 행 단위 출력)
# 문2 : 주사위를 두 번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 출력
print("----문제1----")

for i in range(2,10):
    for j in range(1,10):
        print(f"{i} * {j} = {i * j}", end= " ")

print("\n---문제2---")
for i in range(6):
    n1 = i + 1
    for j in range(6):
        n2 = j + 1
        n = n1 + n2
        if n % 4 == 0:
            print(n1, n2)

print()
for i in range(1, 7, 1):
    for j in range(1, 7, 1):
        su = i + j
        if su % 4 == 0: print(i, j)

print("\nend")

