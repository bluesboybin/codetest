'''
1. 회원관리 hash table : dict
    key:id, value: 로그인 여부 (1/0)
    로그인된 회원수 찾을 때는 sum(d.values()) -> O(n)로 비효율적이므로 전역변수 loginCnt 에 계속 +/- 관리
2. 회원관리 + 로그인회원관리 : set x 2개
'''

import sys
sys.stdin = open('input10.txt')
input = sys.stdin.readline

# 1번 풀이
# D = {}      # D[id]=login(1/0)
# loginCnt = 0
# for _ in range(int(input())):
#     cmd, id = input().split()
#     if cmd == '1':
#         print(int(id in D))
#     elif cmd == '2':
#         print(int(id in D and id in D[id]))     # D[id]가 먼저 나오면 에러 발생할 수 있음
#     elif cmd == '3':
#         if id not in D: D[id] = 0
#         print(len(D))
#     elif cmd == '4':
#         if id in D:
#             if D[id]:
#                 loginCnt -= 1
#                 del D[id]
#         print(len(D))
#     elif cmd == '5':
#         if id in D and D[id]==0:
#             D[id]+=1
#             loginCnt+=1
#         print(loginCnt)     # print(sum(D.values()) <- O(n)으로 계산되므로 시간이 오래 걸림. 그래서 전역변수로 관리
#     else:
#         if id in D and D[id]:
#             D[id] = 0
#             loginCnt -=1
#
# 2번 풀이
member = set()
login = set()
for _ in range(int(input())):
    cmd, id = input().split()
    if cmd == '1':
        print(int(id in member))
    elif cmd == '2':
        print(int(id in login))     # D[id]가 먼저 나오면 에러 발생할 수 있음
    elif cmd == '3':
        member.add(id)
        print(len(member))
    elif cmd == '4':
        # if id in member: member.remove(id)
        member -= {id}              # 코드 상으로는 차집합쓰는게 이뻐 보이긴 함
        login -= {id}
        print(len(member))
    elif cmd == '5':
        if id in member: login.add(id)
        print(len(login))
    else:
        login -= {id}
        print(len(login))