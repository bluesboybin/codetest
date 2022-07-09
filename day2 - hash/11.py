import sys
sys.stdin = open('input11.txt')
input = sys.stdin.readline

d = {}          # str : cnt
prefix = set()

for _ in range(int(input())):
    value = input().strip()
    if value not in d:
        d[value] = 1
        # prefix 작업
        cnt = 0
        for i in range(len(value)):
            temp = value[0:i+1]
            if temp not in prefix:
                prefix.add(temp)
                if cnt == 0:
                    print(temp)     # 별칭 출력
                    cnt+=1
        if cnt == 0:
            print(value)    # 
    else:
        d[value] += 1
        print(value + str(d[value]))    # str + cnt 출력