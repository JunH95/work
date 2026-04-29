# Queue : FIFO 구조
from collections import deque

queue = deque()
print('놀이공원 기구 대기 시작')

# 줄서기
queue.append('철수')
print('첫번째 줄서기 : ', list(queue))

queue.append('영희')
print('두번째 줄서기 : ', list(queue))

queue.append('민수')
print('세번째 줄서기 : ', list(queue))

# 놀이기구 탑승
first_person = queue.popleft()
print(first_person, '탑승 완료!')
print('남은 대기자 : ', list(queue))


class Queue:
    def __init__(self, iterable=None):
        self._data = deque()
        if iterable is not None:
            for x in iterable:
                self.enqueue(x)

    def enqueue(self, x):
        self._data.append(x)
        return x

    def dequeue(self):
        if self.is_empty():
            raise IndexError('큐가 비어 있음')
        return self._data.popleft()
    
    def front(self):
        if self.is_empty():
            raise IndexError('큐가 비어 있음')
        return self._data[0]

    def size(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def clear(self):
        self._data.clear()

    def __repr__(self):
        return f'Queue(front -> back {list(self._data)})'


def demo1Func():
    imsi1 = Queue()
    imsi2 = Queue([10, 20, 30])
    print(imsi1)
    print(imsi2)
    print("imsi2에서 가장 앞에 있는 값 : ", imsi2.front())
    print()
    
    q = Queue()
    for item in ['A', 'B', 'C', 'D']:
        q.enqueue(item)
        print(f'enqueue {item} -> {q}')

    print('FIFO에 따라 하나씩 추출')
    while not q.is_empty():
        print(f'dequeue -> {q.dequeue()} | now: {q}')


def demo2Func(jobs, ppm=15):
    q = Queue(jobs)
    t_sec = 0.0
    order = []

    print('\n프린터로 출력하기')
    while not q.is_empty():
        doc, pages = q.dequeue()
        duration = (pages / ppm) * 60.0
        t_sec += duration
        order.append(doc)
        print(f't={t_sec:6.1f}초 | 출력 : {doc:10s}({pages}페이지)')


if __name__ == '__main__':
    demo1Func()
    print('\n문서 프린터로 출력 시뮬레이션')
    jobs = [('abc.pdf', 10), ('nice.doc', 30), ('good.txt', 5)]
    demo2Func(jobs, ppm=20)
