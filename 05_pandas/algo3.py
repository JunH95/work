# 리스트 안에 들어 있는 자료를 오름차순 정렬
# 4 병합 정렬 : 배열을 반으로 나눈 뒤 각각 정렬하고, 다시 합치면서 정렬

# 방법 1 : 이해 위주 (재귀 호출과 pop을 활용해 직관적으로 구현)
def merge_sort(a):
    n = len(a)
    # 종료 조건: 정렬할 리스트의 자료 개수가 1개 이하이면 정렬할 필요가 없음
    if n <= 1:
        return a
    
    # 리스트를 반으로 나누어 두 그룹으로 쪼갬
    mid = n // 2
    g1 = merge_sort(a[:mid]) # 앞부분 재귀 호출로 정렬
    g2 = merge_sort(a[mid:]) # 뒷부분 재귀 호출로 정렬
    
    result = []
    # 두 그룹에 자료가 남아 있는 동안 반복
    while g1 and g2:
        # 두 그룹의 맨 앞 자료 값을 비교하여 작은 값을 뽑아내어 결과 리스트에 추가
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
            
    # 위 과정을 마치고 남은 자료들을 결과에 모두 추가 (둘 중 하나는 이미 비어 있음)
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
        
    return result

d = [2, 4, 5, 1, 3]
print(merge_sort(d))


# 리스트 안에 들어 있는 자료를 오름차순 정렬
# 4. 병합 정렬 (표준 인덱스 포인터 방식)

def merge_sort(a):
    n = len(a)
    if n <= 1:
        return
    
    # 1. 리스트를 반으로 나눔
    mid = n // 2
    left = a[:mid]
    right = a[mid:]
    
    # 2. 나뉜 부분들을 재귀 호출로 각각 정렬
    merge_sort(left)
    merge_sort(right)
    
    # 3. 정렬된 두 그룹을 하나로 합침 (인덱스 사용)
    i = 0  # left 그룹의 인덱스
    j = 0  # right 그룹의 인덱스
    k = 0  # 원본 리스트 a의 인덱스
    
    # 양쪽 그룹에 모두 데이터가 남아있는 동안 비교하여 작은 값을 원본 리스트에 덮어씀
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
        
    # 만약 left 그룹에 데이터가 남았다면 마저 채워 넣음
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
        
    # 만약 right 그룹에 데이터가 남았다면 마저 채워 넣음
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1

d = [2, 4, 5, 1, 3]
merge_sort(d)
print("병합 정렬 결과:", d)