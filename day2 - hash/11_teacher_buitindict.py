import sys
from collections import defaultdict

sys.stdin = open('input11.txt')
input = sys.stdin.readline  # 이렇게 input 안받으면 속도 오래 걸릴 수 있음...

'''
str의 prefix가 이전에 등장했는지 판단, prefix를 등록
    => prefix set
str 등장한 횟수 판단
    => dict(key=str, value=cnt)
'''
prefix = set()
wcnt = defaultdict(int)

for _ in range(int(input())):
    word = input().strip()
    # print(word)
    sub = ''
    done = 0
    for ch in word:
        sub += ch
        if sub not in prefix:
            if done == 0:
                print(sub)
                done = 1
            prefix.add(sub)
    wcnt[word] += 1     # defaultdict로 선언한 경우 word가 없을 때 wcnt[word] 코드가 접근하자마자 wcnt[word]=0이 등록됨
                        # word가 key로 있는지 없는지 체크할 필요없음
    if done == 0:
        cnt = wcnt[word]
        if cnt == 1:    print(word)
        else:   print(word, cnt, sep='')