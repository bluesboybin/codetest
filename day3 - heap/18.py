import sys
from collections import defaultdict
from heapq import heappush, heappop

sys.stdin = open('input18.txt')
input = sys.stdin.readline

D = defaultdict(int)
maxpq, minpq = [], []
for _ in range(int(input())):
    cmd, value, cnt = map(int, input().split())
    # print(cmd, worth, cnt)
    if cmd == 1:
        D[value] += cnt
        heappush(maxpq, -value)
        heappush(minpq, value)
        print(D[value])
    elif cmd == 2:
        D[value] = max(D[value]-cnt, 0)
        print(D[value])
    else:
        # 강사님 코드
        # pq = maxpq if value else minpq
        # ret = 0
        # while cnt and pq:
        #     worth = abs(pq[0])
        #     if D[worth] == 0:   # 두부가 없으면 해당 worth를 pop!!!!
        #         heappop(pq)
        #         continue
        #     sellcnt = min(cnt, D[worth])
        #     D[worth] -= sellcnt
        #     cnt -= sellcnt
        #     ret += worth * sellcnt
        #
        # print(ret)
        # 내코드1...runtime 에러 발생
        sales = 0
        pq = maxpq if value else minpq
        while cnt>0 and pq:
            worth = abs(heappop(pq))  # 이 부분이 문제....유효하지 않을 때 pop() 해야 한다....
            if D[worth]:
                if D[worth] > cnt:
                    sales += cnt * worth
                    D[worth] -= cnt
                    break
                else:
                    sales += worth * D[worth]
                    cnt -= D[worth]
                    # del D[worth]
        print(sales)

        # # 내코드2...runtime 10점
        # sales = 0
        # pq = maxpq if value else minpq
        # while cnt and pq:
        #     worth = abs(heappop(pq))
        #     if D[worth] > cnt:
        #         sales += cnt * worth
        #         print(sales)
        #         D[worth] -= cnt
        #         break
        #     else:
        #         sales += worth * D[worth]
        #         cnt -= D[worth]
        #         del D[worth]

# print(D)
# 3*2 + 2*3 + 1*2 = 14