# 436 ms

# import #
import sys
import copy


# class #
class Solution:
    max_n: int = 5
    dt: list[list[int]] = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def move(self, board: list[list[int]], dy: int, dx: int):
        start_y, start_x = 0, 0
        if dy == 1:         # 아래쪽
            start_y = 0
        elif dy == -1:      # 위쪽
            start_y = len(board) - 1
        elif dx == 1:       # 오른쪽
            start_x = 0
        else:               # 왼쪽
            start_x = len(board) - 1
            
        stack = []
        for i in range(len(board)):
            y, x = start_y, start_x # 블록을 놓을 위치(커서)

            # 한 쪽 끝에서 다른 한 쪽 끝으로 이동하면서 블록을 스택에 저장
            while 0 <= y < len(board) and 0 <= x < len(board):
                if board[y][x] != 0:
                    stack.append((y, x))
                y, x = y + dy, x + dx    
            y, x = y - dy, x - dx

            # 스택에서 하나씩 뽑으면서 위치 이동
            while stack:
                r, c = stack.pop()  # 현재 이동시킬 블록의 위치
                # 두 위치가 하나의 블록을 가리키고 있다면
                if (y, x) == (r, c):
                    continue

                # 두 블록의 값이 같다면
                if board[y][x] == board[r][c]:
                    board[y][x] += board[r][c]
                    board[r][c] = 0
                    y, x = y - dy, x - dx
                # 블록을 놓을 위치가 비어있다면
                elif board[y][x] == 0:
                    board[y][x] = board[r][c]
                    board[r][c] = 0
                # 두 경우 모두 아니라면
                else:
                    stack.append((r, c))
                    y, x = y - dy, x - dx

            # 다음에 순회할 행 또는 열 이동
            start_y, start_x = start_y + abs(dx), start_x + abs(dy)

        return
    
    
    def _2048(self, board: list[list[int]], n: int) -> int:
        if n >= self.max_n:
            return max(map(max, board))

        result = 0
        for dy, dx in self.dt:
            board_copy = copy.deepcopy(board)
            self.move(board_copy, dy, dx)
            result = max(result, self._2048(board_copy, n + 1))
        
        return result


# main #
if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip('\n'))
    board = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]

    print(Solution()._2048(board, 0))
