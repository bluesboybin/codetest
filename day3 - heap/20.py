import sys
from heapq import heappush

sys.stdin = open('input20.txt')
input = sys.stdin.readline

# n, m (n: 1<scout id<10,000, m: 1<player id <10,000 )

# scout 별로 평가한 player 점수
# sum, avg각각 min/max heapq 생성하고, heapq에 tuple을 push: (총점, sid)

cnt = []   # cnd[pid] = 평가 횟수       m+1 list
scoreAll = []    # scoreAll[pid] = 선수 총점 m+1 list
sum_minpq, sum_maxpq = [], []
avg_minpq, avg_maxpq = [], []
eval = []           # sid가 평가한 pid의 마지막 score

n, m = map(int, input().split())
# print(n, m)
cnt = [0] * (m+1)
scoreAll = [0] * (m+1)
eval = [[0] * (m+1) for _ in range(n+1)]

# lazy_update!
for _ in range(int(input())):
    cmd = list(input().split())
    # print(cmd)
    if cmd[0] == 'EVAL':
        sid, pid, score = map(int,cmd[1:])
        # print(sid, pid, score)

        if eval[sid][pid] > 0:
            scoreAll -= eval[sid][pid] + score
        else:
            scoreAll += score
            cnt += 1
            eval[sid][pid] = score

    elif cmd[0] == 'CLEAR':
        pass
    elif cmd[0] == 'SUM':
        pass
    else:
        pass