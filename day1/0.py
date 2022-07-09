#test code: file로 입력받기
import sys
sys.stdin = open('input0.txt') # 테스트용 파일 읽기 코드
# a = input() # 느려서 이거 잘 안씀
# a = sys.stdin.readline() # 이걸 씀
input = sys.stdin.readline
a = input()
print(a)

b = input().split()
# 형변환 str -> int
print(list(map(int, b)))

c = list(map(int, input().split()))
print(c)

