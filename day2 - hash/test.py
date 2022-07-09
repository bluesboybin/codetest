'''
Day-2 테스트 코드 작성

'''
import random

d = {}
s = set()
s = {1, 2, 3}
print(type(d), type(s))
s.add(1)
s.add(2)
s |= {3, 4, 5}      # 합집합 연산자 |
print(s)
s -= {4, 5, 6}      # 차집합 연산자 -, 없는 값 뺄 때 에러 없음
# s.remove(6)         # remove 함수는 없는 값 뺄 때 에러 발생
print(s)
s &= {2}            # 교집합 연산자 &
print(s)
print('---------------------------------------------')
A = [[0] * 5 for _ in range(5)]
print(A)
print('---------------------------------------------')


# N=5, M=2
N=5
M=2
A = [[0] * N for _ in range(N)]
B = [[0] * M for _ in range(M)]
for i in range(N):
    for j in range(N):
        A[i][j] = random.randint(0, 1)
print('A: ', A)
r = random.randint(0, N-M)  # N-M=3, 0, 1, 2
c = random.randint(0, N-M)
print('r c :', r, c)
zero = 1
for i in range(M):
    for j in range(M):
        B[i][j] = A[r + i][c + j]
        if B[i][j]: zero = 0
print('B: ', zero, B)

'''
1 0 1 0 0
1 0 1 0 0
0 1 0 0 1
0 1 0 1 0
0 0 0 1 0

0 0
0 0
'''

