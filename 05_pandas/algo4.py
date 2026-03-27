# 리스트 안에 들어 있는 자료를 오름차순 정렬
# 5 퀵 정렬 : 기준점(Pivot)을 정해 기준점보다 작은 데이터는 왼쪽, 큰 데이터는 오른쪽으로 모으는 분할 정복 방식입니다

# 방법 1 : 이해 위주 (pop을 사용하지 않고 for문으로 구현하여 원본 보존)
def quick_sort(a):
    n = len(a)
    # 종료 조건: 정렬할 리스트의 자료 개수가 1개 이하이면 정렬할 필요가 없음
    if n <= 1:
        return a
    
    pivot = a[-1] # 맨 마지막 값을 기준점(pivot)으로 설정 (값만 복사해 옴)
    group1 = []   # 기준점보다 작은 값을 담을 리스트
    group2 = []   # 기준점보다 큰 값을 담을 리스트
    
    # 마지막 값(pivot)을 제외하고 처음부터 끝 직전까지 반복
    for i in range(0, n - 1):
        if a[i] < pivot:
            group1.append(a[i])
        else:
            group2.append(a[i])
            
    # 재귀 호출로 각각 정렬한 후 합쳐서 반환
    return quick_sort(group1) + [pivot] + quick_sort(group2)

d = [2, 4, 5, 1, 3]
print(quick_sort(d))
print(d) # 원본 리스트 d가 파괴되지 않고 [2, 4, 5, 1, 3] 그대로 남아있음!


# 방법 2 : 일반 알고리즘 (새로운 리스트를 만들지 않고 리스트 안에서 직접 정렬)
def quick_sort2_sub(a, start, end):
    # 종료 조건: 정렬할 구간이 1개 이하면 종료
    if end - start <= 0:
        return
    
    # 기준점을 구간의 마지막 값으로 정함
    pivot = a[end]
    i = start
    
    # start부터 end 직전까지 반복하며 기준점과 비교
    for j in range(start, end):
        if a[j] <= pivot:
            # 기준점보다 작거나 같으면 앞쪽(i 위치)으로 보내고 i를 1 증가
            a[i], a[j] = a[j], a[i]
            i += 1
            
    # 반복문이 끝나면 i 위치에는 기준점보다 큰 값이 있으므로, 기준점과 자리를 바꿈
    a[i], a[end] = a[end], a[i]
    
    # 기준점을 중심으로 왼쪽 구간과 오른쪽 구간을 각각 다시 퀵 정렬 (재귀 호출)
    quick_sort2_sub(a, start, i - 1)
    quick_sort2_sub(a, i + 1, end)

# 사용자가 쓰기 편하게 포장해 주는 껍데기 함수
def quick_sort2(a):
    quick_sort2_sub(a, 0, len(a) - 1)

d = [2, 4, 5, 1, 3]
quick_sort2(d)
print(d)