# 1892 ms

# import
import sys
import heapq
import math


# global
answer = 0


# function
def find(a):
    if p[a] == a:
        return a

    p[a] = find(p[a])
    return p[a]


def union(a, b):
    p[find(b)] = find(a)


def mst():
    global answer
    
    pq = []
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if adj_arr[i][j]:
                heapq.heappush(pq, (0, i, j))
            else:
                heapq.heappush(pq, (math.sqrt((pos[i][0] - pos[j][0]) ** 2 + (pos[i][1] - pos[j][1]) ** 2), i, j))
    
    while pq:
        cost, A, B = heapq.heappop(pq)
        if find(A) == find(B):
            continue
        answer += cost
        union(A, B)


# main
N, M = map(int, sys.stdin.readline().rstrip('\n').split())
pos = [(0, 0)] + [tuple(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]
adj_arr = [[False for __ in range(N + 1)] for _ in range(N + 1)]
p = [_ for _ in range(N + 1)]
for i in range(M):
    A, B = map(int, sys.stdin.readline().rstrip('\n').split())
    adj_arr[A][B] = True
    adj_arr[B][A] = True

mst()

print(format(answer, ".2f"))
