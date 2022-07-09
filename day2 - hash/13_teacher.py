import sys
from collections import defaultdict

sys.stdin = open('input13.txt')
input = sys.stdin.readline

K = int(input())
dna = input().strip()
htab = defaultdict(int)

# 1번 풀이: dna를 sorting한 고유값을 key로 hash table에 등록
# for i in range(len(dna)-K+1):
#     htab[''.join(sorted(dna[i:i+K]))]+=1
# print(max(htab.values()))

# 2번 풀이: tuple을 hash key로
key = [0, 0, 0, 0]  # [A, C, G, T]
idx = {'A':0, 'C':1, 'G':2, 'T':3}
for i in range(len(dna)):
    key[idx[dna[i]]]+=1
    if i>=K:
        key[idx[dna[i-K]]] -= 1
    if i>=K-1:
        htab[tuple(key)] += 1
print(max(htab.values()))