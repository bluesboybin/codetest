### main.py ###
import sys
from solution41 import init, getCount, getMaxArea

CMD_INIT = 1
CMD_COUNT = 2
CMD_AREA = 3


def run():
    numQuery = int(sys.stdin.readline())
    isCorrect = False
    land = [[0 for _ in range(20)] for __ in range(20)]
    structure = [0 for _ in range(5)]

    for q in range(numQuery):
        inputs = iter(sys.stdin.readline().split())
        cmd = int(next(inputs))

        if cmd == CMD_INIT:
            N = int(next(inputs))
            for i in range(N):
                for j in range(N):
                    land[i][j] = int(next(inputs))
            init(N, land)
            isCorrect = True

        elif cmd == CMD_COUNT:
            M = int(next(inputs))
            for i in range(M):
                structure[i] = int(next(inputs))
            userAns = getCount(M, structure)
            ans = int(next(inputs))
            if userAns != ans:
                isCorrect = False

        elif cmd == CMD_AREA:
            M = int(next(inputs))
            for i in range(M):
                structure[i] = int(next(inputs))
            seaLevel = int(next(inputs))
            userAns = getMaxArea(M, structure, seaLevel)
            ans = int(next(inputs))
            if userAns != ans:
                isCorrect = False

    return isCorrect


if __name__ == '__main__':
    sys.stdin = open('input41.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])

    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)