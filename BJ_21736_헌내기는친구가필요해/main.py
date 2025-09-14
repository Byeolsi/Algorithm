# 768 ms

# import #
import sys
from collections import deque


# main #
if __name__ == "__main__":
    dt = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    N, M = map(int, sys.stdin.readline().rstrip('\n').split())
    campus = [list(sys.stdin.readline().rstrip('\n')) for _ in range(N)]
    visited = [[False for __ in range(M)] for _ in range(N)]
    q = deque()
    answer = 0

    # 도연이 위치 찾기
    for y in range(N):
        for x in range(M):
            if campus[y][x] == 'I':
                q.append((y, x))
                visited[y][x] = True

    while q:
        y, x = q.popleft()
        if campus[y][x] == 'P':
            answer += 1
        
        for dy, dx in dt:
            ry, rx = y + dy, x + dx
            if ry < 0 or ry >= N or rx < 0 or rx >= M:
                continue
            if visited[ry][rx]:
                continue
            if campus[ry][rx] == 'X':
                continue
            
            q.append((ry, rx))
            visited[ry][rx] = True

    if answer == 0:
        print("TT")
    else:
        print(answer)
