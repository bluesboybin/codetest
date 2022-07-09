# LinkedList를 구현하는 문제는 python에서는 잘 안나온다.....왜냐하면 내장 함수가 없기 때문에 직접 만들어야 함.
# 시간과 노력이 많이 들어가니까 LinkedList로는 안풀고, 다른 형태로 푼다.
# 시간복잡도 생각해보면, 문자열 한 개가 추가될 때마다 index를 +1, -1 등의 미루는 연산으로 선형적으로 해야 되므로, O(N^2)
# 문제에서 N=100만이면 N^2은 못푼다. 1000정도면 그냥 N^2 방법으로 풀어도 무방

import sys

sys.stdin = open('input4.txt')
input = sys.stdin.readline

pwds = []
# setting
N = int(input())
for _ in range(N):
    pwds.append(input())
# print(pwds)

for pwd in pwds:
    cursor = 0
    result = ''
    len = 0
    for i in range(len(pwd)):   # i는 읽는 순서
        if pwd[i] == '<':
            if len-1<0:
                pass
            else:
                cursor-=1

        elif pwd[i] == '>':
            if len-1>i:
                pass
            else:
                cursor+=1

        elif pwd[i] == '-':
            result = result[:cursor-1] + result[cursor:]
        else:
            result = result[:cursor] + pwd[cursor] + result[cursor:]
            len += 1
            cursor+=1

