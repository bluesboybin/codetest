## 1. tuple, list 대소비교
print('tuple, list 대소비교')
a = (1, 2, 3)
b = (3, 1, 2)
print(a<b) # 앞 원소일수록 우선순위 높음
a = [1, 2, 3]
b = [1, 2, 5]
print(a<b) # 앞 원소일수록 우선순위 높음
print('--------------------------------------')

## 2. Dict
# hashtable 기반 검색, key값 검색 빠름
# x값 검색 list는 linear search O(n), dict는 hash search O(상수)
from heapq import nsmallest, nlargest
D = dict()
D = {'a':1, 'b':2, 'c':3}
print(D.keys())
print(D.items())
print('--------------------------------------')

A = [1, -3, 5, 2, -2, 2, 7, 10]
print(nsmallest(3, A))      # O(n log k)
print(sorted(A)[:3])        # O(n log n)
print(nlargest(3, A))       # O(n log k)
print(sorted(A))
print(nsmallest(4, A, key=abs))
print(nsmallest(4, A, key=lambda x: (abs(x), x)))
print('--------------------------------------')


## 3. list multiplication
dice = [[0] * 6]*6  # list가 뻥튀기 되서 list reference를 복사하는 것. 특정 dice[i][j]를 바꿔도 복사된 영역 전체가 바뀜
dice[1][3] = 100
print(dice)
dice = [0] * 6      # primitive 라서 뻥튀기 안됨
dice[0] = 3
print(dice)
print('--------------------------------------')
