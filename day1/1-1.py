# 수열

import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline
A = []
# def comp(x):
#     return (abs(x), x)    #tuple : immutable, 변경불가능, 메모리 작음, 연산빠름 vs. list: mutable, 변경가능, 메모리 큼, 연산느림

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
            A.insert(0, value)  # o index position에 value 삽입

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

            # for i in range(len(A)-1, -1, -1):
            #     if A[i] > value:
            #         del A[i]
            #         cnt += 1
            #         if cnt >= 3: break
            #     i -= 1

    elif cmd[0] == 3:
        value = cmd[1]
        # print('before: ', A)
        # key parameter는 heap에 사용되고, 함수 형태로 쓸 예정
        # A.sort(key=abs)   # -3 => 3, -5 => 5 로 바꿔서 sort
        # A.sort(key=comp)    # -3 => key:(3, -3), -5 => (5, -5), 3=> (3, 3)
        # A.sort(key=lambda x : (abs(x), x))  # key=comp와 동일

        A.sort(key=lambda x: (abs(value-x), x))
        # print('after: ', A)


    else:
        if cmd[1] == 0:
            # for i in range(len(A)):
            #     print(A[i], end=' ')
            # print()
            print(*A)
        else:
            print(*A[::-1])