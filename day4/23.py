'''
i=1,    [6:7] <=>[7:8]
i=2,     [4:6] <=> [6:8]
i=3,    [2:5] <=> [5:8]
..      [len-i*2:len-i]
        [len-2:len-1]
'''
import sys
sys.stdin = open('input23.txt')
input = sys.stdin.readline

n = int(input())

A = [0] * n
def isBad(len):
    i=1
    while len-i*2>=0:
        if A[len-i*2:len-i] == A[len-i:len]:
            return 1
        i+=1
    return 0
def recur(c):   # c번 index를 채워라
    #base condition
    if c>=n:
        print(*A, sep='')
        return 1
    # normal condition
    for i in range(1, 4):
        A[c] = i
        if isBad(c+1): continue
        success = recur(c+1)
        if success: return 1
    return 0
recur(0)