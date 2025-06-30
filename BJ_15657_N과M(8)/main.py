# 68 ms

# import
import sys


# function
def print_array(selected):
    for i in selected:
        print(array[i], end=' ')
    print()


def perm(selected, index, prev):
    if index >= M:
        print_array(selected)
        return

    for i in range(prev, N):
        selected.append(i)
        perm(selected, index + 1, i)
        selected.pop()


# main
N, M = map(int, sys.stdin.readline().rstrip('\n').split())
array = list(map(int, sys.stdin.readline().rstrip('\n').split()))
array.sort()

perm([], 0, 0)
