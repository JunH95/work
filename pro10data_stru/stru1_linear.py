# linearlist 선형 구조
# 놀이공원 줄서기
# 연습1 - python 함수 사용
line = ['철수', '영희', '민수']
print('현재 줄 상태 : ', line)
print()

# 데이터 접근 - 인덱싱
print('첫번째 사람 : ', line[0])
print('두번째 사람 : ', line[1])
print()

# 데이터 삽입 - insert()
line.insert(2, '지수') # 민수 다음자리로 밀림
print('지수 삽입 후 줄 상태 : ', line)
print()

# 데이터 삭제
line.remove('영희') # 1번째 이후 자료가 앞으로 한칸씩 이동
print('영희 삭제 후 줄 상태 : ', line)
print()

# 앞사람 부터 놀이기구 타기 - 첫번째 자료부터 빠져나감 뒤자료는 앞으로 이동
first_person = line.pop(0)
print('첫번째 사람 입장 후 남은 줄 상태 : ', line)
print()

# 현재 남은 사람 번호와 함께 출력
for i, p in enumerate(line):
    print(i, '번째 사람 : ', p)
print('**' * 10)

# 연습2 - 함수 사용하지 않고 구현
line = ['철수', '영희', '민수']
print('현재 줄 상태 : ', line)
print()

# 데이터 접근 - 인덱싱
print('첫번째 사람 : ', line[0])
print('두번째 사람 : ', line[1])
print()

# 중간에 새로운 사람 삽입 - 지수를 민수 앞에 끼워넣기
# index 2 위치에 지수 삽입 - 공간확보 뒤로 한칸씩 이동  값 대입
line.append(None) # 빈 공간 확보
for i in range(len(line)-1, 2, -1):
    line[i] = line[i-1]
line[2] = '지수'
print('지수 삽입 후 줄 상태 : ', line)
print()

# 줄에서 대기하던 사람 포기 - 삭제
remove_index = None
for i in range(len(line)):
    if line[i] == '영희':
        remove_index = i
        break
if remove_index is not None:
    for i in range(remove_index, len(line)-1): # 삭제할 위치부터 끝까지 한칸씩 앞으로 이동
        line[i] = line[i+1]
    line.pop() # 마지막 자료 삭제
print('영희 삭제 후 줄 상태 : ', line)
print()

# 앞사람 부터 놀이기구 타기
# 앞에서 부터 한칸씩 앞으로 이동
first_person = line[0]
for i in range(0, len(line)-1):
    line[i] = line[i+1]
line.pop()
print('첫번째 사람 입장 후 남은 줄 상태 : ', line)
print()

# linearlist는 index로 즉시 접근 가능, 삽입/삭제는 데이터 이동 발생 - 비효율적
