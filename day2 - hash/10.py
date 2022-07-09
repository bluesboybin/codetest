import sys
sys.stdin = open('input10.txt')
input = sys.stdin.readline

reg = set()
logon = set()

for _ in range(int(input())):
    cmd, id = input().split()
    # print(cmd, id)
    if cmd == '1':
        print(int(id in reg))   # id in reg true -> 1, false -> 0
    elif cmd == '2':
        print(int(id in logon)) # id in logon true -> 1, false -> 0
    elif cmd == '3':
        if id in reg:
            print(len(reg))
        else:
            reg.add(id)
            print(len(reg))
    elif cmd == '4':
        if id in reg:
            reg.remove(id)
            if id in logon:
                logon.remove(id)
        print(len(reg))
    elif cmd == '5':
        if id in reg and id not in logon:
            logon.add(id)
        print(len(logon))
    else:
        if id in logon:
            logon.remove(id)
        print(len(logon))


