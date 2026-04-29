# 연결된 리스트(linked list)
# 자료를 임의의 공간에 기억시키고, 순서에 따라 포인터로 자료를 연결시킨 구조

# 놀이공원 줄서기
class Node:
    def __init__(self, data):
        # 데이터와 다음 노드를 가리키는 next
        self.data = data
        self.next = None

# 연결 리스트 관리 클래스
class LinkedList:
    def __init__(self):
        self.head = None # 맨 앞 노드

    # 새로운 Node를 추가(줄 뒤에 다음 사람 추가)
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        # 줄의 맨 끝 사람 찾기
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def show(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("끝")

    def insert_after(self, target_data, new_data):
        current = self.head
        while current:
            if current.data == target_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"{target_data}를 찾을 수 없습니다.")

    # 특정 노드 삭제
    def remove(self, data):
        # 맨 앞사람이 나가는 경우
        if self.head and self.head.data == data:
            self.head = self.head.next
            return

        # 중간이나 끝사람이 나가는 경우
        current = self.head
        while current and current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        print(f"{data}를 찾을 수 없습니다.")


if __name__ == '__main__':
    line = LinkedList()
    line.append("철수")
    line.append("영희")
    line.append("민수")

    print("현재 줄 상태:")
    line.show()
    print()

    # 영희 뒤에 지수를 삽입
    print("영희 뒤에 지수 삽입:")
    line.insert_after("영희", "지수")
    line.show()
    print()

    # 영희가 줄서기를 포기 (삭제)
    print("영희 삭제:")
    line.remove("영희")
    line.show()