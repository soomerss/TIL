# Abstarct Data Structures
#
# 추상적 자료구조 : 자료구조의 내부 구현은 숨겨두고, 밖에서 보이는 것들 두가지를 제공하는 자료구조를 말한다하나는 데이터, 다른 하나는 일련의 연산

class Node():
    def __init__(self,item):
        self.data = item
        self.next = None

class LinkedList():
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

# 연산 정의
# 1. 특정 원소 참조 (k번째) - 1부터 시작하는 노드로 쓰고 0은 다른 목적으로 # pos가 뭐지
    def get_at(self,pos):
        if pos <= 0 or pos > self.nodeCount :
            return None
        i = 1
        cuur = self.head
        while i < pos :
            curr = curr.next
            i += 1
        return curr
# 2. 리스트 순회
    def traverse(self):
        answer = []
        i = 1
        while i <= self.nodeCount:
# 3. 길이 얻어내기
# 4. 원소삽입
# 5. 원소 삭제
# 6. 두 리스트 합치기

# 배열과 비교한 연결 리스트
|구분     |   배열     |   연결리스트|
|저장공간| 연속한 위치| 임의의 위치|
|특정 원소 지칭 | 매우 간편 -O(1) | 선형탐색과 유사 - O(n)|



