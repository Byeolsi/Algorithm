# 72 ms

# import #
import sys
from collections import deque


# class
class Solution:
    dt: list[int] = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def __init__(self, N: int):
        self.N = N
        self.visited = [[False for __ in range(N)] for _ in range(N)]


    def isVisited(self, y: int, x: int) -> bool:
        return self.visited[y][x]
    

    # BFS 탐색을 통해 색상 구역을 확인
    def bfs(self, image: list[list[int]], y: int, x: int, ch: str):
        q = deque()
        q.append((y, x))
        self.visited[y][x] = True

        while q:
            y, x = q.popleft()

            for dy, dx in dt:
                ry, rx = y + dy, x + dx
                if ry < 0 or ry >= self.N or rx < 0 or rx >= self.N:
                    continue
                if self.visited[ry][rx]:
                    continue
                # 다른 문자인 경우
                if image[ry][rx] != ch:
                    continue

                q.append((ry, rx))
                self.visited[ry][rx] = True


# main #
if __name__ == "__main__":
    dt = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    N = int(sys.stdin.readline().rstrip('\n'))
    image = [list(sys.stdin.readline().rstrip('\n')) for _ in range(N)]
    answer1, answer2, = 0, 0

    # 적록색약이 아닌 사람
    sol1 = Solution(N)
    for i in range(N):
        for j in range(N):
            if sol1.isVisited(i, j):
                continue
            sol1.bfs(image, i, j, image[i][j])
            answer1 += 1

    # 모든 'G'를 'R'로 변경
    for i in range(N):
        for j in range(N):
            if image[i][j] == 'G':
                image[i][j] = 'R'

    # 적록색약인 사람
    sol2 = Solution(N)
    for i in range(N):
        for j in range(N):
            if sol2.isVisited(i, j):
                continue
            sol2.bfs(image, i, j, image[i][j])
            answer2 += 1

    print(answer1, answer2)
