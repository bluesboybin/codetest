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
sys.stdin = open('input26.txt')
input = sys.stdin.readline

w, h = map(int, input().split())
# print(h,w)
A = [list(input().strip()) for _ in range(w)]
# print(A)

visit = [[0] * w for _ in range(h)]
# print(visit)

dx = [-1, 0, 1, 0]  # 위, 아래, 우, 좌
dy = [0, 1, 0, -1]

def dfs(x, y):          # (x, y)를 방문, return (x, y)포함한 (x, y)를 통해 방문한 모든 좌표 개수 return
    visit[x][y] = 1
    cnt = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위를 벗어난 경우 체크
        if nx<0 or nx>=h or ny<0 or ny >=w: continue
        # 목장이 아닌 경우
        if A[nx][ny] == ',': continue
        # 이미 방문한 곳인 경우
        if visit[nx][ny]: continue
        cnt += dfs(nx, ny)
    return cnt

ret = 0
for i in range(h):
    for j in range(w):
        if A[i][j] == '*':
            ret = max(ret, dfs(i, j))
print(ret)