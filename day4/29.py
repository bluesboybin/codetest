'''
010010
011011

000 - 100, 010, 001
0 - 4, 2, 1
001 - 101, 011, 000
1 - 5, 3, 0
010 - 110, 000, 011
2 - 6, 0, 3
'''


import sys
from collections import deque

sys.stdin = open('input29.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
A= {}           # value: 코드 queue
for i in range(1, n+1):
    str = input().strip()
    value = 0
    for j in range(k):
        value += int(str[j])*2**(k-1-j)
        A[value].append(i)
print(A)
f, t = map(int, input().split())
