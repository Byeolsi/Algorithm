# 48 ms

# import
import sys
import heapq


# global
dt = [[0, 1], [1, 0], [0, -1], [-1, 0]]


# function
def bfs(i, j):
    answer = 0

    # 우선순위 큐 사용
    pq = []
    visited[i][j] = True
    heapq.heappush(pq, (grid[i][j], i, j))
    while pq:
        weight, i, j = heapq.heappop(pq)
        # 끝 지점에 도달하면 바로 반환
        # 가장 처음으로 도달한 루트가 최소 누적 가중치로 도달한 루트이기 때문
        if (i, j) == (N - 1, N - 1):
            return weight

        for dy, dx in dt:
            y = i + dy
            x = j + dx
            if y < 0 or y >= N or x < 0 or x >= N or visited[y][x]:
                continue
            visited[y][x] = True
            # 현재까지 가중치를 누적해서 추가
            # 그래야만 누적 가중치가 가장 낮은 지점을 우선적으로 탐색
            heapq.heappush(pq, (weight + grid[y][x], y, x))


# main
N = int(sys.stdin.readline().rstrip('\n'))
grid = [list(sys.stdin.readline().rstrip('\n')) for _ in range(N)]
# 가중치 계산을 위해 '0'을 1로, '1'을 0으로
for i in range(N):
    for j in range(N):
        if grid[i][j] == '0':
            grid[i][j] = 1
        else:
            grid[i][j] = 0
visited = [[False for __ in range(N)] for _ in range(N)]

print(bfs(0, 0))
