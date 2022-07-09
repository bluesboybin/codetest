import sys
from collections import defaultdict

sys.stdin = open('input13.txt')
input = sys.stdin.readline

d = defaultdict(int)
k = int(input())
text = input().strip()
# print(k, text)
max = 0
for i in range(len(text)-k+1):
    # print(text[i:i+k])
    mark = text[i:i+k]      # sliding window 구현시 이전 걸 활용하는 방식은 아니었음
    # A:4*4*4=64, C:4*4=16, G:4, T:1
    key = 0
    for ch in mark:
        if ch == 'A':   key+=1000000000
        elif ch == 'C': key+=1000000
        elif ch == 'G': key+=1000
        else:   key+=1
    d[key] += 1
    if max < d[key]:
        max = d[key]
print(max)

