'''
sid 1~n => 큰 값
pid => pname
avg = 소수 둘째자리 반올림

player[pname] = [sum, avg, cnt] => dict(key:pname, value:[sum, avg, cnt])

scouter[1~n] = {pid:score,... } => dict(key:sid, value:dict)

heap (sum, pname), avg, pname)
'''

import sys
from collections import defaultdict
from heapq import heappush, heappop, heapify

sys.stdin = open('input21.txt')
input = sys.stdin.readline

n, m = map(int,input().split())

class Player:
    def __init__(self):
        self.sum = 0
        self.cnt = 0
        self.avg = 0

    def update(self, ds, dc):
        self.sum+=ds
        self.cnt+=dc
        self.avg=round(self.sum*10/self.cnt) if self.cnt else 0 # *10한 상태(int)로 관리

P = {}                   # P[pname] = Player(sum,cnt,avg)
S = defaultdict(dict)    # S[sid] = { pname:score , .., }  , S[sid][pname] = score

class MinData:
    def __init__(self, val, pname):
        self.val = val
        self.pname = pname
    def __lt__(self, other):
        return (self.val, self.pname) < (other.val, other.pname)

class MaxData:
    def __init__(self, val, pname):
        self.val = val
        self.pname = pname
    def __lt__(self, other):
        return (self.val, self.pname) > (other.val, other.pname)

maxsum = []     # MaxData(sum, pname)
minsum = []     # MinData(sum, pname)
maxavg = []     # MaxData(avg, pname)
minavg = []     # MinData(avg, pname)

def push(pname):
    heappush(maxsum, MaxData(P[pname].sum, pname))
    heappush(minsum, MinData(P[pname].sum, pname))
    heappush(maxavg, MaxData(P[pname].avg, pname))
    heappush(minavg, MinData(P[pname].avg, pname))

names = input().split()
for i in range(m):
    P[names[i]] = Player()
    push(names[i])      # heap 초기화

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0]=='EVAL':
        sid, pname, score = int(cmd[1]), cmd[2], int(cmd[3])
        #if sid not in S: S[sid] = {}   <= defaultdict으로 대체
        if pname in S[sid]:
            P[pname].update(score-S[sid][pname], 0)
        else:
            P[pname].update(score, 1)
        S[sid][pname] = score
        push(pname)

    elif cmd[0]=='CLEAR':
        sid = int(cmd[1])
        for pname, score in S[sid].items():
            P[pname].update(-score, -1)
            push(pname)
        del S[sid]

    elif cmd[0]=='SUM':
        flag = int(cmd[1])
        pq = maxsum if flag else minsum
        while pq[0].val != P[pq[0].pname].sum:
            heappop(pq)
        print(pq[0].pname)

    else:
        flag = int(cmd[1])
        pq = maxavg if flag else minavg
        while pq[0].val != P[pq[0].pname].avg:
            heappop(pq)
        print(pq[0].pname)

