# 리스트 안에 들어 있는 자료를 오름차순 정렬
# 3 버블 정렬 : 서로 인접한 두 원소를 검사하여 정렬

# 방법 1 : 이해 위주
# 리스트를 한 번 훑으면서 가장 큰 값을 맨 뒤로 밀어내고, 그 값을 뽑아내는 함수
def bubble_pass(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]  # 두 값의 위치를 바꿈
    return a.pop()  # 가장 큰 값이 맨 뒤로 밀려났으므로 뽑아서 반환

def bub_sort(a):
    result = []
    while a:
        max_val = bubble_pass(a)  # 남은 리스트에서 가장 큰 값을 하나씩 가져옴
        result.insert(0, max_val) # 큰 값을 계속 맨 앞에 넣어야 오름차순 정렬이 됨
    return result


# 리스트 안에 들어 있는 자료를 오름차순 정렬
# 1. 버블 정렬 (표준 및 최적화 방식)

def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        change = False
        
        # 매 패스(Pass)마다 가장 큰 값이 맨 뒤로 확정되므로 비교 범위를 줄임 (n - 1 - i)
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]  # 자리 바꿈
                change = True
                
        # 한 번도 자리를 바꾸지 않았다면 이미 정렬이 완료된 것이므로 반복문 종료
        if not change:
            break

d = [2, 4, 5, 1, 3]
bubble_sort(d)
print("버블 정렬 결과:", d)