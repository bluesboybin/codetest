import sys
sys.stdin = open('input11.txt')
input = sys.stdin.readline  # 이렇게 input 안받으면 속도 오래 걸릴 수 있음...

'''
str의 prefix가 이전에 등장했는지 판단, prefix를 등록
    => prefix set
str 등장한 횟수 판단
    => dict(key=str, value=cnt)
'''
prefix = set()
wcnt = {}

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
    if word not in wcnt:
        wcnt[word] = 1
        if done == 0:
            print(word)
    else:
        wcnt[word] += 1
        if done == 0:
            # print(word, wcnt[word], sep='')
            print('%s%d' % (word, wcnt[word]))