import sys
sys.stdin = open('input3.txt')
input = sys.stdin.readline

A = []
for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == '1':
        A.append(cmd[1].lower())
        # print(A)

    elif cmd[0] == '2':
        if cmd[1] == '0':
            A.sort()
        elif cmd[1] == '1':
            A.sort(reverse=1)
        else:
            A.sort(key=lambda s: (len(s), s))   # 1순위 len(s), 2순위 s
        print(*A[:3])
    elif cmd[0] == '3':
        A[0] += cmd[1].lower()      # 덧붙이기
        A[0] = A[0][:15]            # 15자 자르기
        print(A[0])