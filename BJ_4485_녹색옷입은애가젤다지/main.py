# import
import sys
import heapq


# global
# 100 ms

dt = [[0, 1], [1, 0], [0, -1], [-1, 0]]


# function
def dijkstra(i, j):
    pq = []
    distances[i][j] = cave[i][j]
    heapq.heappush(pq, (cave[i][j], i, j))

    while pq:
        cost, i, j = heapq.heappop(pq)

        if distances[i][j] < cost:
            continue

        for dy, dx in dt:
            y, x = i + dy, j + dx
            if y < 0 or y >= N or x < 0 or x >= N:
                continue
            cost_to = cost + cave[y][x]
            if distances[y][x] > cost_to:
                distances[y][x] = cost_to
                heapq.heappush(pq, (cost_to, y, x))


# main
t = 1
while True:
    N = int(sys.stdin.readline().rstrip('\n'))
    if N == 0:
        break

    cave = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]
    distances = [[10 * N for __ in range(N)] for _ in range(N)]

    dijkstra(0, 0)

    print("Problem {}: {}".format(t, distances[-1][-1]))
    t += 1
