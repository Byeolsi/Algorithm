# 72 ms

# import
import sys
from collections import deque


# main
answer = []
dt = [[0, 1], [1, 0], [0, -1], [-1, 0]]

N, M, K = map(int, sys.stdin.readline().rstrip('\n').split())
sqr = [[False for _ in range(M)] for _ in range(N)]

# 직사각형에 해당하는 범위를 True로 설정
for k in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip('\n').split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            sqr[y][x] = True

# bfs
dq = deque()
for i in range(N):
    for j in range(M):
        if sqr[i][j]:
            continue

        cnt = 1
        dq.append((i, j))
        sqr[i][j] = True
        while dq :
            n, m = dq.pop()
            for dy, dx in dt:
                y = n + dy
                x = m + dx
                if y < 0 or y >= N or x < 0 or x >= M or sqr[y][x]:
                    continue
                cnt += 1
                dq.append((y, x))
                sqr[y][x] = True
        answer.append(cnt)

answer.sort()
print(len(answer))
print(' '.join(list(map(str, answer))))
