'''
heap: 부모 노드의 우선순위가 자식 노드의 우선순위보다 높다
    stack : 나중에 들어온 데이터가 먼저 나감
    queue: 먼저 들어온 데이터가 먼저 나감
    priority queue: 우선 순위가 높은 데이터가 먼저 나감 (※ prioirity queue != heap 이나 거의 같은 말임)

(1) heap의 연산복잡도 push(), pop() 1번의 연산비용은 노드 개수가 N일 때, O(log N)
(2) 완전이진트리는 list 하나면 구현 가능 (1차원 배열 하나로 구현 가능)
    list [13, 8, 10, 2, 6]
    x의 부모 노드 = (x-1) / 2
    x의 왼쪽 자식 = x * 2 + 1
    x의 오른쪽 자식 = x * 2 + 2
    
(3) python에는 
    heapq : 빠른 편. 검정에서 씀. 우선순위 key값 설정 못하므로 무조건 value가 작은게 top()에 들어가도록 되어 있음
    priority queue : 실시간 thread 처리하는데 좋아서 실무적으로는 좋은데 (안정성은 높으나 느림...그래서 검정에선 안씀)
    heapq의 heappush(), heappop() 함수를 쓸 때는 heap이 있다는 가정이 있으므로, 그냥 list에 다가 heappush(), heappop()쓰면 안된다.
        그래서 heapify()를 하고 난 다음에 push(), top() 함수 쓸 것
'''
import sys
from heapq import heapify, heappush, heappop

sys.stdin = open('input15.txt')
input = sys.stdin.readline

# maxpq = [ 10, 1, 2, 3, 4, 5, 6]
# print(maxpq)
# heapify(maxpq)                  # O(N)
# print(maxpq)
# heappush(maxpq,1)
# heappop(maxpq)
# print(maxpq[0])

maxpq, minpq, abspq = [], [], []
for _ in range(int(input())):
    x = int(input())
    if x == 0:  # pop
        if minpq:
            print(-heappop(maxpq), heappop(minpq), heappop(abspq)[1])
        else:
            print(-1)
    else:        # push
        heappush(minpq, x)
        heappush(maxpq, -x)
        heappush(abspq, (abs(x), x))        # 절대값 작은게 우선순위가 더 높음



