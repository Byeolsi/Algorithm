# 1368 ms

# import
import sys


# global
dt = [[0, 1], [1, 0], [0, -1], [-1, 0]]


# function
def dfs(i, j):
    for dy, dx in dt:
        y, x = i + dy, j + dx
        if y < 0 or y >= N or x < 0 or x >= N or \
               grid[y][x] <= k or visited[y][x]:
            continue
        visited[y][x] = True
        dfs(y, x)


# main
sys.setrecursionlimit(10**6)

answer = 0

N = int(sys.stdin.readline().rstrip('\n'))
grid = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]
mx = max(sum(grid, []))
mn = min(sum(grid, []))

for k in range(mn - 1, mx):
    visited = [[False for __ in range(N)] for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] <= k or visited[i][j]:
                continue
            visited[i][j] = True
            dfs(i, j)
            result += 1
    answer = max(answer, result)

print(answer)
