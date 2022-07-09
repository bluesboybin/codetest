'''
이동 위치 8방향
=> dx, dy로 이동 가능한 방향을 미리 셋팅

dfs로 할 경우는 최소 이동(탐색??) 횟수를 보장하지 않기 때문에, bfs를 쓴다.
이미 방문한 곳은 별도 처리
    visit[x][y] = 1/0
    que = [(x, y, cnt)]

    visit[x][y] = cnt/-1
    que = [(x, y)]
'''

import sys
from collections import deque

sys.stdin = open('input27.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
sx, sy, ex, ey = map(int, input().split())  # 말 (x, y) 졸 (x, y)
visit =[[0] * (m+1) for _ in range(n+1)]
dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

def bfs():
    que = deque([(sx, sy, 0)])
    visit[sx][sy] = 1
    while que:
        x, y, cnt = que.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx<1 or nx>n or ny<1 or ny>m: continue
            if visit[nx][ny]: continue
            que.append((nx, ny, cnt+1))
            visit[nx][ny] = 1
            if((nx, ny)) == (ex, ey):
                return cnt+1
    # return -1
print(bfs())