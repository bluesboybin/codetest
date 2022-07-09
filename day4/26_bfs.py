'''
2차원 배열 탐색 - flood filee => 자주 나오는 듯
그래프 탐색
트리 탐색

<탐색 방법>
dfs : 재귀 (스택), ※ 검정에서도 stack 메모리 제한이 있음 1MB
                    stack memory: 지역변수, 매개변수가 stack memory를 쓰는데
                                  dfs로 재귀함수 쓸 때 stack overflow 발생 가능 (depth가 10,000 넘어가면 발생할 수 있음)
bfs : 큐, 탐색을 하는데 최단 경로(길이)를 구한다면 dfs 말고 bfs로 풀어야 한다.

한 번 방문한 곳은 다시 가지 않도록 별도 표시
1) visit[x][y] = 1/0
2) 원본을 유지할 필요가 없으면 원본 변경

※ bfs, dfs 를 바꿔서 만드는 방법을 숙지?
'''

import sys
from collections import deque

sys.stdin = open('input26.txt')
input = sys.stdin.readline

w, h = map(int, input().split())
# print(h,w)
A = [list(input().strip()) for _ in range(h)]
# print(A)

visit = [[0] * w for _ in range(h)]
# print(visit)

dx = [-1, 0, 1, 0]  # 위, 아래, 우, 좌
dy = [0, 1, 0, -1]

def bfs(sx, sy):        # O(w*h*4) 방문한 곳의 개수 * 4
    que = deque([(sx, sy)])
    A[sx][sy] = '.'     # visited check, 빈 공간으로 변경처리

    cnt=1         # que에 들어간 횟수. bfs 함수가 호출됐을 때 1번 que에 들어갔으니 초기값은 1로 설정
    while que:      # que에 원소가 있는 동안
        x, y = que.popleft()    # 가장 먼저 들어온 * 좌표를 x, y로 받고 나서 que에서 삭제
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=h or ny<0 or ny>=w: continue
            if A[nx][ny] == '.': continue   # (nx, ny)가 빈공간이거나 방문한 곳이면 다시 for문 처음으로
            que.append((nx, ny))
            A[nx][ny] = '.'     # que에 중복된 값이 들어가는 것을 막기 위해서
            cnt += 1
    return cnt

ret = 0
for i in range(h):
    for j in range(w):
        if A[i][j] == '*':
            # dfs(i, j)
            # visit[i][j] = 1
            ret = max(ret, bfs(i, j))
print(ret)