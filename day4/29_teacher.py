'''
<그래프로 구하는 방법>
1-2
1-3
2-5
2-4
3-5

인접리스트 => list or dict 로 구현
adj[x] = [인접한 번호,...]
1 | 2 3
2 | 1 4 5
3 | 1 5
4 | 2
5 | 1 3

queue = [ (방문체크, 거리) ]
visit = [ ]

                dist        |   prev
A | C E | 0                     X(시작이니까)
B | D   | -1| 3                 D
C | A D | 1                     A
D | B C |-1 | 2                 C
E | A   |1                      A

목적지 도착하면 visit에 넣고, 그것의 prev를 저장,
'''

import sys
from collections import deque

sys.stdin = open('input29.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
code = [''] + [input().strip() for _ in range(N)]
# print(code)
###그래프 구성###
adj = [[] for _ in range(N+1)]

def getDist(a, b):
    dist = 0
    for i in range(K):
        if a[i] != b[i]: dist+=1
    return dist
for i in range(1, N+1):
    for j in range(1, i):
        if getDist(code[i], code[j]) == 1:
            adj[i].append(j)
            adj[j].append(i)
# print(adj)
### BFS
prev = [-1] * (N+1)

s, e = map(int, input().split())
def printPath(x):
    path = []
    while x:
        path.append(x)
        x = prev[x]
    print(*path[::-1])
def bfs(s, e):
    que = deque([s])
    prev[s] = 0
    while que:
        x = que.popleft()
        for y in adj[x]:
            if prev[y]>=0: continue
            que.append(y)
            prev[y] = x
            if y == e:
                printPath(e)
                return
    print(-1)
bfs(s, e)