'''
땅 좌표을 (1,1)~(n,n) 으로 사용하고 0, n+1 위치는 바다로 표현
bfs시에 (0,0)에서 시작하면 잠기는 모든 땅 확인 가능
'''
from collections import defaultdict, deque

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]  # 우, 하, 좌, 상


def key(li):
    minv = min(li)
    return ''.join(map(lambda x: str(x - minv), li))


def key2(li):
    maxv = max(li)
    return ''.join(map(lambda x: str(maxv - x), li))


def init(N, Land):
    global n, m, L, D
    n, m = N, N + 2  # m=테두리에 바다를 포함했을 때의 크기
    L = [[0] * m] + [[0] + Land[i][:n] + [0] for i in range(n)] + [[0] * m]  # 실제 땅 좌표를 (1,1)~(n,n) 으로 사용
    D = defaultdict(list)
    for len in range(1, 6):
        for i in range(1, n + 1):
            for j in range(1, n - len + 2):
                s = key(L[i][j:j + len])
                D[s].append((i, j, 0))
                if len == 1: continue
                if s != s[::-1]: D[s[::-1]].append((i, j + len - 1, 2))

                s = key([L[x][i] for x in range(j, j + len)])
                D[s].append((j, i, 1))
                if s != s[::-1]: D[s[::-1]].append((j + len - 1, i, 3))


def getCount(M, structure):
    return len(D[key2(structure[:M])])


def bfs(level):
    q = deque([(0, 0)])  # (0,0)을 시작으로 bfs를 돌려주면 된다.
    visited = [[0] * m for _ in range(m)]
    visited[0][0] = 1
    remain = m ** 2
    while q:
        x, y = q.popleft()
        remain -= 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= m: continue
            if L[nx][ny] >= level: continue
            if visited[nx][ny]: continue
            q.append((nx, ny))
            visited[nx][ny] = 1

    return remain


def getMaxArea(M, structure, seaLevel):
    global L
    ret = -1
    for x, y, dir in D[key2(structure[:M])]:
        for i in range(M):
            L[x + dx[dir] * i][y + dy[dir] * i] += structure[i]

        ret = max(ret, bfs(seaLevel))

        for i in range(M):
            L[x + dx[dir] * i][y + dy[dir] * i] -= structure[i]
    return ret