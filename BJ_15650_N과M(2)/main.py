# 44 ms

# import
import sys


# function
def perm(selected, index, prev):
    if index >= M:
        print(' '.join(list(map(str, selected))))
        return

    for i in range(prev + 1, N + 1):
        selected.append(i)
        perm(selected, index + 1, i)
        selected.pop()


# main
N, M = map(int, sys.stdin.readline().rstrip('\n').split())

perm([], 0, 0)
