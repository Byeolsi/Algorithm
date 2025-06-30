# 156 ms

# import
import sys


# functions
def dfs(i, j):
    if i == N - 1 and j == M - 1:
        return 1

    # 중요: 이미 방문한 경로라면, 해당 경로를 통해 갈 수 있는 모든 경로의 가지 수 반환
    if visited[i][j]:
        return dp[i][j]
    visited[i][j] = True
    
    for dy, dx in dt:
        y = i + dy
        x = j + dx
        if y < 0 or y >= N or x < 0 or x >= M:
            continue
        if maps[i][j] <= maps[y][x]:
            continue
        # 모든 가능한 방향으로 DFS 탐색
        dp[i][j] += dfs(y, x)

    # 해당 경로를 통해 갈 수 있는 모든 경로의 가지 수 반환
    return dp[i][j]


# constants
dt = [ (-1, 0), (0, 1), (1, 0), (0, -1) ]


# main
N, M = map(int, sys.stdin.readline().rstrip('\n').split())
maps = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]
visited = [[False for __ in range(M)] for _ in range(N)]
dp = [[0 for __ in range(M)] for _ in range(N)]

print(dfs(0, 0))
