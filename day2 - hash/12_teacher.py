import sys
from collections import defaultdict

sys.stdin = open('input12.txt')
input = sys.stdin.readline

'''
land[N][N] = pid / 미점령
2차원 배열을 쓸 경우, N<=100,000 이므로 100,000 * 100,000 이므로 memory를 너무 쓴다. 최소 1차원
(1) 땅상태 확인하기
    key=(x,y)   value=땅 상태
(2) pid 별 점령한 땅 수   cnt[pid] = 점령땅수

'''
cnt = [0] * 4   # cnt[pid] = 점령개수
land = {}       # land[(x,y)] = pid     점령되지 않은 경우 등록 안됨
n, q = map(int, input().split())
for i in range(q):
    pid = i % 4
    x, y = map(int,input().split())
    key = (x, y)                # tuple은 dict, set에서 key로 설정 가능. int, str, tuple ()은 hashable type
    if key in land:
        pid2 = land[key]
        if pid == pid2:
            del land[key]
            cnt[pid] -= 1
        elif cnt[pid] < cnt[pid2]:
            land[key] = pid
            cnt[pid] += 1
            cnt[pid2] -= 1
    else:
        land[key] = pid
        cnt[pid] += 1
# for i in range(len(cnt)):
#     print(cnt[i])
print(*cnt, sep='\n', end='')