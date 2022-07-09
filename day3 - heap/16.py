import sys
from heapq import heappush
from heapq import heappop

sys.stdin = open('input16.txt')
input = sys.stdin.readline

'''
L (mid 값) R
그룹에 원소 추가
L: 가장 큰 값 선별 / 삭제
R: 가장 작은 값 선별 / 삭제
O(N) * 턴

min() or max()  : O(n) * 턴
heap : O(log n) * 턴

heap
L: maxheap
R: minheap
mid: int
'''
L = []  # max
R = []  # min

n = int(input())
mid = int(input())
print(mid)

def Lpush(x): heappush(L, -x)
def Rpush(x): heappush(R, x)
def Lpop(x): return -heappop(L)
def Rpop(x): return heappop(R)
for i in range(n//2):
    for x in map(int, input().split()):
        if x < mid: heappush(L, -x)
        else: heappush(R, x)
    if len(L) < len(R):
        heappush(L, -mid)
        mid = heappop(R)

    if len(L) > len(R):
        heappush(R, mid)
        mid = -heappop(L)
    print(mid)