# LinkedList를 구현하는 문제는 python에서는 잘 안나온다.....왜냐하면 내장 함수가 없기 때문에 직접 만들어야 함.
# 시간과 노력이 많이 들어가니까 LinkedList로는 안풀고, 다른 형태로 푼다.
# 시간복잡도 생각해보면, 문자열 한 개가 추가될 때마다 index를 +1, -1 등의 미루는 연산으로 선형적으로 해야 되므로, O(N^2)
# 문제에서 N=100만이면 N^2은 못푼다. 1000정도면 그냥 N^2 방법으로 풀어도 무방


# 왼쪽 list, 오른쪽 deque or list
# insert : 왼쪽 뒤에 추가  O(1)
# erase : 왼쪽 뒤 삭제     O(1)
# left : 왼쪽 뒤 삭제      O(1)
#         오른쪽 앞 삽입    O(1)
# right : 오른쪽 앞 삭제    O(1)
#         왼쪽 뒤 삽입     O(1)

import sys

sys.stdin = open('input4.txt')
input = sys.stdin.readline

for _ in range(int(input())):
    log = input().strip()
    L, R = [], []
    for ch in log:
        if ch=='<':
            if L:   R.append(L.pop())
            print(L, R)
        elif ch=='>':
            if R:   L.append(R.pop())
            print(L, R)
        elif ch=='-':
            if L:   L.pop()
            print(L, R)
        else:
            L.append(ch)
            print(L, R)
    # print(L+R[::-1])
    # print(''.join(L+R[::-1]))