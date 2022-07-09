import sys
sys.stdin = open('input9.txt')
input = sys.stdin.readline

'''
대소문자 구분 X, 문자열 id별 score를 관리하므로 set 보다는 dict가 적합
'''
n = 0
D = {}  # D[string] = [id, score]

for _ in range(int(input())):
    s, score = input().split()
    s = s.lower()
    score = int(score)

    if s in D:
        D[s][1] = max(D[s][1], score)
    else:
        n+=1
        D[s] = [n, score]
    print(*D[s])