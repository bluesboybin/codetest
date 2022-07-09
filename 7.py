import sys
from collections import deque

sys.stdin = open('input7.txt')
input = sys.stdin.readline

'''
각 방법 별 연산시간을 분석해 볼 것
(1) 1차원으로 관리 (제일 쉽게 만들 수 있음.....) => move는 빠르지만 insert/erase가 느리다
<list> ※ deque에 대해서 잘 모르겠음....언제 list 대신 deque를 써야 할 지 공부할 것...
- cur = x*m+y , x = cur/m , y = cur%m
- insert: O(LEN<1,000,000) * 10,000회
- erase: O(LEN<1,000,000) * 10,000회
- move: O(1) * 100,000회

(2) 2차원으로 관리 : 메모장 사이즈 보다 행+1 x 열+1 사이즈로 생성
<2차원 list>
- cur = x*m+y , x = cur/m , y = cur%m
- insert: O(N*M=len) * 10,000회
- erase: O(N*M=len) * 10,000회
- move: O(1) * 100,000회
<2차원 deque> => 이 방식으로 구현 결정
- cur = x*m+y , x = cur/m , y = cur%m
- insert: O(N+M) *10,000회
- erase: O(N+M) * 10,000회
- move: O(1) * 100,000회

(3) 커서 기준 그룹 분류
- keylogger (day1-4.py) 문제처럼 커서 기준 왼쪽, 오른쪽 그룹 분류 방식
<list: L, R>
- cur = x*m+y , x = cur/m , y = cur%m
- insert: L.append O(1)*10,000회
- erase: L.pop O(1)*10,000회
- move: O(N*M)*100,000회

=> (3)의 move 계산복잡도가 다른 방식의 모든 연산보다 크기 때문에 제일 느릴 것으로 보임
=> 가장 오래 걸리는 연산을 개선할 수 있는 아이디어가 필요함
=> 자료를 표현하는 방법의 공간 (len) 뿐만 아니라 수행 횟수도 고려
'''

n, m, q = map(int, input().split())
init = input().strip()  # 문자열 공백제거
# print(init)
memo = [deque() for _ in range(n)]
# print(memo)

cnt, cur = 0, 0
for ch in init:
    memo[cnt//m].append(ch)
    cnt+=1
# print(memo)

for _ in range(q):
    cmd = input().split()
    if cmd[0] == 'insert':
        x, y = cur//m, cur%m
        memo[x].insert(y, cmd[1])       # O(m)  모든 열에 수행
        while len(memo[x])>m:   # M보다 크면...다음줄로 옮기는 것을 무한 반복 , O(n) 모든 행에 수행
            memo[x+1].appendleft(memo[x].pop())
            x+=1
        cur+=1
        cnt+=1

    elif cmd[0] == 'erase':
        if cur == 0: continue   # 예외 상황
        cur-=1  # 지워야 할 ch 좌표로 커서를 이동
        cnt-=1
        x, y = cur//m, cur%m
        del memo[x][y]      # O(m)
        while memo[x+1]:    # 원소가 있으면 true, 없으면 false   O(n)
            memo[x].append(memo[x+1].popleft())
            x+=1

    else:
        x, y = int(cmd[1]), int(cmd[2])
        cur = min(x*m+y, cnt)
        if cur==cnt: print('*')
        else: print(memo[x][y])