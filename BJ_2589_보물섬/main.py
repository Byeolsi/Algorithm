# 572 ms

# import
import sys
from collections import deque


# global
dt = [[0, 1], [1, 0], [0, -1], [-1, 0]]


# function
def bfs(i, j):
    q = deque()
    visited[i][j] = True
    q.append((i, j))
    size = len(q)
    depth = 0

    # (i, j) 기준 depth를 계산하여 거리 계산
    while q:
        i, j = q.popleft()
        size -= 1
            
        for dy, dx in dt:
            y, x = i + dy, j + dx
            if 0 <= y < N and 0 <= x < M and \
                   grid[y][x] == 'L' and not visited[y][x]:
                visited[y][x] = True
                q.append((y, x))

        if q and size <= 0:
            size = len(q)
            depth += 1

    return depth
                

# main
answer = 0

N, M = map(int, sys.stdin.readline().rstrip('\n').split())
grid = [list(sys.stdin.readline().rstrip('\n')) for _ in range(N)]

# 모든 위치를 기준으로 거리를 계산
for i in range(N):
    for j in range(M):
        if grid[i][j] == 'L':
            # 위, 아래에 모두 육지가 존재한다는 것은 육지의 더 끝자락이 존재한다는 의미
            if 0 <= i - 1 < N and 0 <= i + 1 < N and \
                   grid[i - 1][j] == 'L' and grid[i + 1][j] == 'L':
                continue
            # 왼쪽, 오른쪽에 모두 육지가 존재한다는 것은 육지의 더 끝자락이 존재한다는 의미
            if 0 <= j - 1 < M and 0 <= j + 1 < M and \
                   grid[i][j - 1] == 'L' and grid[i][j + 1] == 'L':
                continue
            visited = [[False for __ in range(M)] for _ in range(N)]
            answer = max(answer, bfs(i, j))
        
print(answer)
