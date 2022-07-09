# 수열

# list
# 삽입 O(n)
# 맨뒤삽입 O(1)
#
# deque
# 삽입 O(1)

import sys
from _collections import deque

sys.stdin = open('input1.txt')
input = sys.stdin.readline
A = deque()

q = int(input()) # input 양식이 처음 첫 줄은 숫자 하나만 있으니까...
for _ in range(q): # 0 ~ q-1
    cmd = list(map(int, input().split()))
    # print(cmd)

    if cmd[0] == 1:
        # pos, value = cmd[1], cmd[2]
        pos, value = cmd[1:]
        if pos == 1:
            A.append(value)     # 값을 뒤에서부터 채울 때
        else:
            A.appendleft(value)  # o index position에 value 삽입

    elif cmd[0] == 2:
        pos, value = cmd[1:]
        cnt = 0
        if pos == 0:
            i = 0
            while i<len(A):
                if A[i] >= value:
                    del A[i]
                    cnt += 1
                    if cnt>=3: break
                else:
                    i+=1
        else:
            i = len(A) - 1
            while i>=0:
                if A[i] >= value:
                    del A[i]
                    cnt += 1
                    if cnt>=3: break
                i-=1

    elif cmd[0] == 3:
        value = cmd[1]
        # A = list(A)
        # A.sort(key=lambda x: (abs(value-x), x))
        # A = deque(A)
        A = deque(sorted(A, key=lambda x: (abs(value-x), x)))       # A를 정렬하는게 아니라 정렬한 list를 반환

    else:
        if cmd[1] == 0:
            print(*A)
        else:
            print(*list(A)[::-1])
            A.reverse   # iterator 역순으로 A를 갱신. A가 갱신되므로 여기서는 안씀