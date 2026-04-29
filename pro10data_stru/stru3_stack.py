# stack : LIFO 구조

stack = []
print('놀이공원 입장')

# 놀이기구 탈 때의 기록 남김
stack.append('T-express 탑승')
print('기록 : ', stack)

stack.append('바이킹 탑승')
print('기록 : ', stack)

stack.append('회전목마 탑승')
print('기록 : ', stack)

# 가장 최근 기록 삭제
if stack:
    last_action = stack.pop()
    print(f'[{last_action}] 기록 취소 후 현재 : ', stack)

if stack:
    last_action = stack.pop()
    print(f'[{last_action}] 기록 취소 후 현재 : ', stack)


class Stack:
    def __init__(self, iterable=None):
        self._data = []
        if iterable is not None:
            for x in iterable:
                self.push(x)

    def push(self, x):
        self._data.append(x)
        return x

    def pop(self):
        if self.is_empty():
            raise IndexError('스택 비어 있음')
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError('스택 비어 있음')
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __repr__(self):
        top_to_bottom = list(reversed(self._data))
        return f'Stack(top -> bottom {top_to_bottom})'


def demo1Func():
    s = Stack()
    print('\n스택 작업 시작')
    for item in ['A', 'B', 'C', 'D']:
        s.push(item)
        print(f'push {item} | {s}')
    
    print('LIFO에 따라 하나씩 추출')
    while not s.is_empty():
        print(f'pop -> {s.pop()} | now: {s}')


if __name__ == '__main__':
    demo1Func()