# 64 ms

# import #
from collections import deque
import sys


# global #
input = sys.stdin.readline


# class #
class Solution:
    def move(self, y, x, dy, dx, board):
        cnt = 0
        # 벽을 만나거나 구슬이 구멍에 빠질 때까지 이동
        while board[y + dy][x + dx] != '#' and board[y][x] != 'O':
            y += dy
            x += dx
            cnt += 1

        return y, x, cnt


    def solve(self, N, M, board, visited):
        # 초기 위치 찾기
        ry = rx = by = bx = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 'R':
                    ry, rx = i, j
                elif board[i][j] == 'B':
                    by, bx = i, j

        # BFS 초기화
        q = deque()
        q.append((ry, rx, by, bx, 0))
        visited[ry][rx][by][bx] = True

        # 상하좌우
        dt = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while q:
            ry, rx, by, bx, depth = q.popleft()
            if depth >= 10:
                continue
            for dy, dx in dt:
                nry, nrx, rc = self.move(ry, rx, dy, dx, board)
                nby, nbx, bc = self.move(by, bx, dy, dx, board)

                # 파란 구슬이 구멍에 빠지면 실패
                if board[nby][nbx] == 'O':
                    continue
                # 빨간 구슬만 구멍에 빠지면 성공
                if board[nry][nrx] == 'O':
                    return depth + 1

                # 둘이 같은 위치라면, 이동한 거리가 긴 쪽을 한 칸 뒤로
                if nry == nby and nrx == nbx:
                    if rc > bc:
                        nry -= dy
                        nrx -= dx
                    else:
                        nby -= dy
                        nbx -= dx

                if not visited[nry][nrx][nby][nbx]:
                    visited[nry][nrx][nby][nbx] = True
                    q.append((nry, nrx, nby, nbx, depth + 1))

        return -1


# main #
if __name__ == '__main__':
    N, M = map(int, input().rstrip('\n').split())
    board = [list(input().rstrip('\n')) for _ in range(N)]
    visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    
    print(Solution().solve(N, M, board, visited))
