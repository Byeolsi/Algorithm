# import
import sys
import collections
import heapq

# global
INF = 100000 * 100000

# main
n = int(sys.stdin.readline().rstrip('\n'))
m = int(sys.stdin.readline().rstrip('\n'))

distance = [[INF for __ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip('\n').split())
    # 경로가 여러 개일 수 있으므로, 그 중 가장 작은 값
    distance[a][b] = min(distance[a][b], c)

# 플로이드 워샬 알고리즘
for k in range(1, n + 1):
    for i in range(1, n + 1):
        if i == k:
            continue
        for j in range(1, n + 1):
            if j == i or j == k:
                continue
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

# print
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if distance[i][j] == INF:
            print('0', end=' ')
        else:
            print(distance[i][j], end=' ')
    print()
