import sys
from collections import defaultdict

sys.stdin = open('input12.txt')
input = sys.stdin.readline

land = {}
cnt = [0] * 4
N, Q = map(int, input().split())
# print(N, Q)

# 5 x 5
# (0, 0) -> 0, (0, 1) -> 1, (0, 2) -> 2, (0, 4) -> 4
# (1, 0) -> 5
# => 좌표 = N x i + j

for i in range(Q):
    n, m = map(int, input().split())
    # print(i, j)
    pid = i % 4    # 누구 명령인지 확인
    cur = n * N + m # 좌표 고유값
    # print(cur)
    if cur in land:     # 땅의 누구 소유가 됐는지?
        pid2 = land[cur]
        if pid == pid2:
            del land[cur]
            cnt[pid] -= 1
        elif cnt[pid] < cnt[pid2]:
            land[cur] = pid
            cnt[pid] += 1
            cnt[pid2] -= 1
    else:
        land[cur] = pid
        cnt[pid]+=1

print(*cnt, sep='\n', end='')

