'''
기초 학습
dict: (key, value), set: key
dict, set은 hash search 이므로 비교횟수 O(1),
list, deque는 linear search 이므로 비교 횟수 O(n), 비교 비용 O(1+)은 문자열인 경우 길이도 찾아야 되므로 O(1)보다 커진다.

Hash는 기본적으로 분류, 인덱싱 기법
bucket size 만큼 % (moduler) 연산해서 각 key에 맞는 bucket을 지정. 같은 bucket에 있는 key들은 linear search로 탐색
keyHash value를 고유하게 만드는 tip, range를 벗어난 값을 곱하는 게 하나의 방법
'''

import sys
sys.stdin = open('input8.txt')
input = sys.stdin.readline

s = set()

for _ in range(int(input())):
    word = input().strip()
    if word in s:               # O(1)
        s.remove(word)
    else:
        s.add(word)

print(len(s))
