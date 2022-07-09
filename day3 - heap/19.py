import sys
from heapq import heappush, heappop

sys.stdin = open('input19.txt')
input = sys.stdin.readline

'''
hash로도 구현은 가능한데, 이럴 경우, 우선순위 기준으로 검색해서 출력할 때 search 연산이 많이 걸린다.
minpq (score, id)
maxpq (-score, -id)

realtime update는 python에서는 만들기 어려우니까 해당 문제는 그냥 패스해라
lazy update 방식을 따르는데, 실제 업데이트되는 정보를 별도 객체로 저장. 
    heap에는 유효하지 않은 item도 있게 되므로 이걸 skip 하는 걸 구현해야 함.
'''

minpq, maxpq = [], []
S = [0] * 100001    # 최신정보 기록 : S[id] = socre 0이면 최신정보 없음

def getThird(pq):
    best = []
    while len(best) < 3 and minpq:
        score, id = heappop(minpq)
        if S[id] != score:  # 최신정보
            continue
        if best and best[-1][1] == id:  # 중복
            continue
        best.append((score, id))
    if len(best) < 3:
        print(-1)
    else:
        print(best[2][1])
    for d in best:
        heappush(minpq, d)

for _ in range(int(input())):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        id, score = cmd[1:]
        S[id] = score
        heappush(minpq, (score, id))
        heappush(maxpq, (-score, -id))
    elif cmd[0] == 2:
        id = cmd[1]
        S[id] = 0
    elif cmd[0] == 3:
        getThird(minpq)
    else:
        getThird(maxpq,)