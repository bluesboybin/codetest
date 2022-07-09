'''
heap 4개
(총점, id) 높은 / 낮은 한 명
(평균, id) 높은 / 낮은 한 명

총점, 평균이 바뀔 때마다 우선순위가 달라짐
=> 총점, 평균이 바뀔 때마다 heap에 새로운 정보를 push
    heap이 push되는 경우
    1. 처음 (0, id) 초기화
    2. Eval(sid, pid, score) 평가됐을 때 pid만 push
    3. Clear(sid) sid가 평가한 모든 pid push

선수 별로 [총점, 평균, 평가인원] 이 관리돼야 함 => list
스카우트별 평가 기록 [ (pid), (score) ] => dict
'''

import sys
from heapq import heappush, heappop, heapify

sys.stdin = open('input20.txt')
input = sys.stdin.readline

n, m = map(int,input().split())

P = [[0,0,0] for _ in range(m+1)]   # P[pid] = [sum, avg, cnt]
S = [{} for _ in range(n+1)]        # S[sid] = { pid:score , .., }  , S[sid][pid] = score
maxsum = []     # (-sum, -pid)
minsum = []     # (sum, pid)
maxavg = []     # (-avg, -pid)
minavg = []     # (avg, pid)

def update(p, ds, dc):
    p[0]+=ds
    p[2]+=dc
    p[1] = round(p[0]/p[2]) if p[2] else 0

def push(pid):
    heappush(maxsum, (-P[pid][0], -pid))
    heappush(minsum, (P[pid][0], pid))
    heappush(maxavg, (-P[pid][1], -pid))
    heappush(minavg, (P[pid][1], pid))

for i in range(1,m+1): push(i)      # heap 초기화

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0]=='EVAL':
        sid, pid, score = map(int,cmd[1:])
        if pid not in S[sid]:   # 평가 안했던 경우
            update(P[pid], score, 1)
        else:
            update(P[pid], score-S[sid][pid], 0)
        S[sid][pid] = score
        push(pid)


    elif cmd[0]=='CLEAR':
        sid = int(cmd[1])
        for pid, score in S[sid].items():    # [(key, value), ... ,]
            update(P[pid], -score, -1)
            push(pid)
        S[sid].clear()


    elif cmd[0]=='SUM':
        flag = int(cmd[1])
        pq = maxsum if flag else minsum

        # 1
        while abs(pq[0][0]) != P[abs(pq[0][1])][0]:
            heappop(pq)
        print(abs(pq[0][1]))

        # 2
        # while 1:
        #     value, pid = map(abs, pq[0])
        #     if value == P[pid][0]:
        #         print(pid)
        #         break
        #     heappop(pq)

    else:
        flag = int(cmd[1])
        pq = maxavg if flag else minavg

        while abs(pq[0][0]) != P[abs(pq[0][1])][1]:
            heappop(pq)
        print(abs(pq[0][1]))