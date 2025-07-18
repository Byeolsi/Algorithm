# import
import sys
import collections

# global
INF = 1000 * 1000

# functions
# BFS 알고리즘
def bfs() -> int:
    q = collections.deque()
    q.append((0, 0, 0))
    visited[0][0][0] = True
    visited[1][0][0] = True
    size, depth = len(q), 1

    while q:
        wall, y, x = q.popleft()
        if (y, x) == (N - 1, M - 1):
            return depth

        for dy, dx in dt:
            u, v = y + dy, x + dx
            if 0 > u or u >= N or 0 > v or v >= M:
                continue
            
            # 길인 경우
            if matrix[u][v] == '0':
                if visited[wall][u][v]:
                    continue
                q.append((wall, u, v))
                visited[wall][u][v] = True
                # 벽을 뚫더라도 벽을 뚥기 전에 지나온 경로는 다시 방문하지 않아야 하므로
                if wall == 0:
                    visited[wall + 1][u][v] = True
            # 벽인 경우
            else:
                # 이미 벽을 한 번 뚫었거나, 이미 방문한 곳인 경우
                if wall == 1 or visited[wall + 1][u][v]:
                    continue
                q.append((wall + 1, u, v))
                visited[wall + 1][u][v] = True

        size -= 1
        if size == 0:
            size = len(q)
            depth += 1

    return -1


# main
N, M = map(int, sys.stdin.readline().rstrip('\n').split())
matrix = [list(sys.stdin.readline().rstrip('\n')) for _ in range(N)]
visited = [[[False for ___ in range(M)] for __ in range(N)] for _ in range(2)]
dt = [[0, 1], [1, 0], [0, -1], [-1, 0]]

print(bfs())
