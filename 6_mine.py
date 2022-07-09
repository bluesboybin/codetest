import sys
sys.stdin = open('input6.txt')
input = sys.stdin.readline

count = 0
order = []

N = int(input())

# setting
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
print(A)

for i in range(N):
    temp = 0
    schedule = [0] * 24
    # print(A[i][1], A[i][2])
    while i<N:
        if max(schedule[A[i][1]:A[i][2]]) == 0:
            schedule[A[i][1]:A[i][2]] = [A[i][0] for x in range(A[i][1], A[i][2])]
            order.append(i)
            temp += 1
        i+=1
    count = max(temp, count)
    print(schedule, 'count: ', count)

