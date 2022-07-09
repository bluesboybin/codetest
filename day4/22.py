import sys
sys.stdin = open('input22.txt')
input = sys.stdin.readline

n,m = map(int, input().split())
# for i in range(1, 7):           # i: 첫 번째 주사위 눈
#     st_j = i if m==2 else 1
#     for j in range(st_j,7):        # j: 두
#         if m==3 and i==j: continue
#         st_k = j if m==2 else 1
#         for k in range(st_k,7):    # k: 세
#             if m==3 and (i==k or j==k): continue
#             print(i,j,k)

dice = [1] + [0] * n
used = [0] * 7
def recur(c):   # c번째 주사위를 던져라
    # base condition
    if c>n:
        print(*dice[1:])
        return

    # normal condition
    st = dice[c-1] if m==2 else 1
    for i in range(st, 7):
        # 같은거 체크하는 방법
        # 1. linear search  O(n)
        # if m==3 and i in dice[1:c]: continue

        # 2. used[i] = 1/0  O(1)
        if m==3 and used[i]: continue

        dice[c] = i
        used[i] = 1
        recur(c+1)
        used[i] = 0

recur(1)