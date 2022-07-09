'''
worth -> cnt
가장 높은 가치 worth
가장 낮은 가치 worth

worth = int 범위
Q <= 200,000
'''
import sys
from collections import defaultdict
from heapq import heappush, heappop

sys.stdin = open('input17.txt')
input = sys.stdin.readline

## 1번 풀이: Hash (key, value) 자료구조인 dict & 가치를 linear 탐색해서 최대최소를 구한 풀이
# d = defaultdict(int)
# Q = int(input())
# for _ in range(Q):
#     cmd, worth = map(int, input().split())
#     # print(cmd, worth)
#     if cmd == 1:  # 두부 생산
#         d[worth] += 1
#         print(d[worth])
#     elif cmd == 2:    # 두부 폐기
#         if d[worth] > 0:
#             d[worth] -= 1
#             print(d[worth])
#             if d[worth] == 0:
#                 del d[worth]
#         else:
#             print(-1)
#             del d[worth]
#     else:
#         if worth == 0:    # 가치 가장 낮은 두부 1개 판매
#             tofu = min(d.keys()) # O(N) * Query 개수
#             if d[tofu] > 0:
#                 d[tofu] -= 1
#                 print(tofu, d[tofu])
#                 if d[tofu] == 0:
#                     del d[tofu]
#         else:             # 가치 가장 높은 두부 판매
#             tofu = max(d.keys())    # O(N) * Query 개수
#             if d[tofu] > 0:
#                 d[tofu] -= 1
#                 print(tofu, d[tofu])
#                 if d[tofu] == 0:
#                     del d[tofu]


## 2번 풀이. 가치와 개수는 dictionary로 가치의 크기는 heapq 2개 minpq, maxpq 를 두고 구하는 풀이
'''
defaultdict
D[worth] = cnt  0이면 삭제 or 유지
maxpq : -worth
minpq : worth
유효한 정보인지 판단 => D[worth] = 0 or 없음 => 유효하지 않음
'''

D = defaultdict(int)
maxpq, minpq = [], []

for _ in range(int(input())):
    cmd, value = map(int, input().split())
    # print(cmd, value)
    if cmd == 1:
        D[value] += 1
        heappush(maxpq, -value)
        heappush(minpq, value)
        print(D[value])
    elif cmd == 2:
        if D[value]:
            D[value] -= 1
            print(D[value])
        else:
            print(-1)

    else:
        pq = maxpq if value else minpq  # value가 1이면 maxpq, 0이면 minpq
        # while D[abs(pq[0])] == 0: heappop(pq)     # 판매한 가치는 pop X
        # worth = abs(pq[0])
        # D[worth] -=1
        # print(worth, D[worth])
        while 1:                                    # 판매한 가치도 pop O
            worth = abs(heappop(pq))
            if D[worth]:
                D[worth] -= 1
                print(worth, D[worth])
                break


