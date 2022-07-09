import sys
sys.stdin = open('input6.txt')
input = sys.stdin.readline

count = 0
order = []

# 끝나는 시간 순서대로 정렬 O(n log n)해서 들어갈 수 있는지 없는지 여부를 선형 탐색 O(log n)
# greedy?
N = int(input())

# setting
A = []
for _ in range(N):
    A.append(tuple(map(int, input().split())))
A.sort(key=lambda x: (x[2]))
# print(A)

End = 0
ret = []
for id, start, end in A:
    if End <= start:
        End = end
        ret.append(id)
print(len(ret))
print(*ret)