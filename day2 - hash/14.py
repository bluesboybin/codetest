import sys
import random

global N, M, A, B
SIZE = 1<<9 # bit 기준으로 2^9  0000 0000 0001 => 0010 0000 0000 로 바꾸는 연산 = 512
htab = [[] for _ in range(SIZE)]        # hash table 만들기
# print(htab)

#############################################################
def gethash(arr, x, y):
    for i in range(3):
        hash = 0
        for j in range(4):
            hash = hash * 2 + arr[x+i][y+j]
    # print(hash)
    return hash


def init():  # N, M, A 활용하여 초기화
    for i in range(SIZE):   htab[i].clear()
    for i in range(N-M+1):
        for j in range(N-M+1):
            htab[gethash(A, i, j)].append(i*N+j)

def isEqual(x, y):
    for i in range(M):
        if A[x+i][y:y+M] != B[i][:M]:  return 0
    return 1

def query():  # B가 A의 (row, col) 위치에서 시작된다고 했을 때,
    # row * N + col 값 반환
    for xy in htab[gethash(B, 0 , 0)]:
        if isEqual(xy//N, xy%N):    return xy
    return 0


#############################################################

def makeArr():
    for i in range(N):
        for j in range(N):
            A[i][j] = random.randint(0, 1)


def makeBrr(limit):
    r = random.randint(0, limit)
    c = random.randint(0, limit)
    zero = 1
    for i in range(M):
        for j in range(M):
            B[i][j] = A[r + i][c + j]
            if B[i][j]: zero = 0
    return zero


def run():
    limit = N - M
    while (makeBrr(limit)): pass
    ret = query()
    userR, userC = ret // N, ret % N
    if userR < 0 or userR > limit or userC < 0 or userC > limit:
        return 0

    for i in range(M):
        for j in range(M):
            if B[i][j] != A[userR + i][userC + j]: return 0

    return 100


if __name__ == '__main__':
    sys.stdin = open('input14.txt', 'r')
    TC = int(sys.stdin.readline())
    global N, M, A, B                       # 전역 변수로 선언되서 다른 함수에서도 사용 가능
    for testcase in range(1, TC + 1):
        N, M, seed, Q = map(int, sys.stdin.readline().split())
        total = 0
        A = [[0] * N for _ in range(N)]
        B = [[0] * M for _ in range(M)]
        makeArr()
        init()
        for _ in range(Q):
            total += run()
        print("#case %d : %d" % (testcase, total // Q))

'''
전체 부분 배열 linear search
쿼리 당, O(부분배열 개수 * 같은지 확인하는 비용) * 총 쿼리 개수 (1000개)
        부분배열 개수: N=7, M=3 (N-M) * (N-M) => N^2 = 1000^2

전체 배열에서 나올 수 있는 모든 부분 배열을 해쉬로 만들어 놓고,
부분배열로 검색하면 O(1)
Dict key = m*m 부분배열, value= row * n + col
    문제는 key 값 길이 400 (25<=M<=400)
    부분배열 개수 = 1,000,000
    Hash 등록 비용 O(n*m*m*a)    a: 충돌난 것에 대한 probing 처리

좌상단 좌표 (row, col) 를 키로 만들어서...
key가 너무 많을 때는 hash함수를 이용해서 샘플링해서 키를 만들어라.

'''