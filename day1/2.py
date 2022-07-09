'''
총 n명 중 우선순위 k명 선별하는 문제로 자주 나온다.
1. heapq : 우선순위 순으로 관리, 선별할 때마다 heap에서 유효한 값 k번 pop
2. min/max: 1명
3. nlargest/nsmallest: 순서없이 관리, 선별할 때마다 검색해서 찾음 (heap 기반)
                        O(n + k log n) : heap에 넣는 연산 O(n) + k개 찾는 연산 O(k log n)
                        O(n log k)
4. 전체 sort: O(n log n) <- quick sort
'''

import sys
from heapq import nsmallest, nlargest

sys.stdin = open('input2.txt')  # 제출할 떄는 제거할 것
input = sys.stdin.readline

D = dict()      # D[pid] = [salary, C, J, P], class 생성해도 됨
q = int(input())

for _ in range(q):
    cmd = input().split()
    if cmd[0] == 'register':
        pid = int(cmd[1])
        D[pid] = list(map(int, cmd[2:]))
        # print(D[pid])

    elif cmd[0] == 'cancel':
        pid = int(cmd[1])
        # print('Before: ', D)
        if pid in D:
            del D[pid]
        # print('After: ', D)

    elif cmd[0] == 'update':
        pid, flag, X = map(int, cmd[1:])
        # print(pid, flag, X)
        if pid in D:
            D[pid][flag+1] = X

    elif cmd[0] == 'hire_min':
        # 1순위 Salary 작은순서, 2순위 pid 작은순서
        pid = min(D, key=lambda pid: (D[pid][0], pid))
        pid = nsmallest(1, D, key=lambda pid: (D[pid][0], pid))[0]
        print(pid)
        del D[pid]

    else:
        # D = [1, 2, 4, 7] dictionary D의 keys
        # [1, 2, 4, 7] => [(3, 1), (37, 2), (0, 4), (30, 7)]
        pids = nlargest(3, D, key=lambda pid: (sum(D[pid][1:]), pid))  # 작을수록 이면 pid => -pid
        print(*pids)
        for pid in pids:
            del D[pid]

