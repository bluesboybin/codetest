'''
이동방향 - 4방향
가장 멀리있는 저글링과의 거리 + 3 => bfs flood fill + 3
1. visit[x][y] = 1/0
    que = (x, y, tick)
    A[1~n][1~m]

2. tick[x][y] = tick / 0 (방문안함=0)
    que = (x, y)
    A[1~n][1~m]

3. map을 어떻게 쓸지?
'''

import sys
from collections import deque

sys.stdin = open('input28.txt')
input = sys.stdin.readline

m, n = map(int, input().split())

A = ['0' * (m+2)] + ['0'+input().strip()+'0' for _ in range(n)] + ['0' * (m+2)]
# print(A)
tick = [[0]*(m+2) for _ in range(n+2)] # 3 이상이면 방문한거고 그 시각에 죽음

sy, sx = map(int, input().split())

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def bfs(sx, sy):
    que = deque([(sx, sy)])
    tick[sx][sy] = 3
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if A[nx][ny] == '0': continue
            if tick[nx][ny]: continue
            que.append((nx, ny))
            tick[nx][ny] = tick[x][y] + 1
    print(tick[x][y])
bfs(sx, sy)
cnt = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if A[i][j] == '1' and tick[i][j] == 0: cnt+=1
print(cnt)