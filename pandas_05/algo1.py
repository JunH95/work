# 리스트 안에 들어 있는 자료를 오름차순 정렬
# 2 삽입 정렬 : 자료 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교하여, 자신의 위치를 찾아 삽입

# 방법 1 : 이해 위주
# 리스트 r에서 v가 들어가야 할 위치를 돌려주는 함수
def find_ins_idx(r, v):
    for i in range(0, len(r)):
        # v가 이미 정렬된 리스트 r의 i번째 값보다 작으면
        # v가 들어갈 자리는 i가 됨
        if v < r[i]:
            return i
    # 적절한 자리를 못 찾았다면(v가 가장 크다면) 맨 뒤로
    return len(r)

def ins_sort(a):
    result = []
    while a:
        value = a.pop(0) # 기존 리스트에서 하나씩 꺼냄
        ins_idx = find_ins_idx(result, value) # 꺼낸 값이 들어갈 위치 찾기
        result.insert(ins_idx, value) # 찾은 위치에 값 삽입
    return result

d = [2, 4, 5, 1, 3]
print(ins_sort(d))


# 리스트 안에 들어 있는 자료를 오름차순 정렬
# 3. 삽입 정렬 (표준 제자리 정렬 방식)

def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]  # 현재 삽입할 타겟
        j = i - 1
        
        # 앞의 값들이 key보다 크면 한 칸씩 뒤로 밀어냄
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            
        # 밀어내기가 끝나고 찾은 알맞은 위치에 key를 삽입
        a[j + 1] = key

d = [2, 4, 5, 1, 3]
insertion_sort(d)
print("삽입 정렬 결과:", d)