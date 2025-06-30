# 232 ms

# import
import sys


# function
def print_array(selected):
    for i in selected:
        print(array[i], end=' ')
    print()


def perm(selected, index):
    if index >= M:
        print_array(selected)
        return

    for i in range(N):
        if visited[i]:
            continue

        selected.append(i)
        visited[i] = True
        perm(selected, index + 1)
        selected.pop()
        visited[i] = False


# main
N, M = map(int, sys.stdin.readline().rstrip('\n').split())
array = list(map(int, sys.stdin.readline().rstrip('\n').split()))
array.sort()
visited = [False for _ in range(N)]

perm([], 0)
