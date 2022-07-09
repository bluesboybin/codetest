import sys
sys.stdin = open('input5.txt')
input = sys.stdin.readline

# 각 주사위 별로 반대 index pair를 저장해서 푸는 방법, 반대 주사위값 pair를 저장해서 푸는 방법
# 주사위가 아니라, 값의 종류가 많은 케이스를 풀 경우에는 index의 경우에는 O(n)의 index search 시간이 소요되므로 value 기반이 더 효율적
# 위, 아랫면 제외한 나머지 값을 구하는 key 설정을 max 함수 내에서 구현해야 함

# dice[i][x] = i번 dice의 x인 값의 반댓면 값
# dice = [[0] * 6 for _ in range(3)]  # list comprehension
# dice[0][3] = 100
# print(dice)

n = int(input())
dice = [[0] * 7 for _ in range(n) ]   # dice[i][x] = i번 주사위의 x인 값의 반대면 값
for i in range(n):
    a, b, c, d, e, f = map(int, input().split())
    # print(a, b, c, d, e, f)
    for x, y in [(a, f), (b, d), (c, e)]:
        dice[i][x], dice[i][y] = y, x
ans = 0
for bottom in range(1, 7):
    ret = 0
    for i in range(n):
        top = dice[i][bottom]
        ret += max(range(1,7), key=lambda x : x if x not in (top, bottom) else 0)
        bottom = top
    ans = max(ans, ret)
print(ans)