'''
1. 0인 위치를 따로 뽑기
2. 숫자 넣을 수 있는지 판단
    2-1. for loop O(9)
    2-2. used   O(1)
            row[x][1~9] = 1/9
            col[y][1~9] = 1/9
            sub[z][1~9] = 1/0
        (x, y) => 그룹좌표 (x/3, y/3) => 그룹id (x*3+y)
        그룹시작 (x*3, y*3)

'''
import sys
sys.stdin = open('input24.txt')
input = sys.stdin.readline

#sudoku = [[0] * 9 for _ in range(9)]
# for i in range(9):
#     sudoku[i] = list(map(int, input().split()))
# print(sudoku)

A = [list(map(int, input().split())) for _ in range(9)]
zero = []
row = [[0] * 10 for _ in range(9)]  # row[x][i] x행에 i를 사용 중이면 1 / 0
col = [[0] * 10 for _ in range(9)]  # col[y][i] x행에 i를 사용 중이면 1 / 0
sub = [[0] * 10 for _ in range(9)]  # col[group_id][i] x행에 i를 사용 중이면 1 / 0

for i in range(9):
    for j in range(9):
        if A[i][j] == 0:
            zero.append(i*9+j)
        else:
            row[i][A[i][j]] = 1
            col[j][A[i][j]] = 1
            sub[(i//3)*3+(j//3)][A[i][j]] = 1

def recur(c):   # zero[c] 위치를 채워라
    if c>=len(zero):
        for i in range(9):
            print(*A[i])
        return 1
    x, y = zero[c]//9, zero[c]%9
    z = (x//3)*3+(y//3)
    for i in range(1, 10):
        # 안되면 continue
        if row[x][i] or col[y][i] or sub[z][i]: continue
        A[x][y] = i
        row[x][i], col[y][i], sub[z][i] = 1, 1, 1
        if recur(c+1):  return 1
        row[x][i], col[y][i], sub[z][i] = 0, 0, 0
    return 0
recur(0)