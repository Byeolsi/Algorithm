# import #
import sys
import copy
from collections import deque


# global #
MAX_CNT = 3
dt = [[0, 1], [1, 0], [0, -1], [-1, 0]]
answer = 0


# function #
# BFS 탐색을 통해 바이러스가 퍼지는 것을 시뮬레이션
def bfs(lab: list[list[int]]):
    q = deque()

    for i in range(len(lab)):
        for j in range(len(lab[i])):
            if lab[i][j] == 2:
                q.append((i, j))

    while q:
        y, x = q.popleft()

        for dy, dx in dt:
            ry, rx = y + dy, x + dx
            if ry < 0 or ry >= len(lab) or rx < 0 or rx >= len(lab[0]):
                continue
            if lab[ry][rx] != 0:
                continue
            q.append((ry, rx))
            lab[ry][rx] = 2

    result = 0
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            if lab[i][j] == 0:
                result += 1

    return result


# 조합을 통해 벽을 세움
def comb(lab: list[list[int]], cnt: int, y: int, x: int):
    global MAX_CNT
    global answer

    if cnt >= MAX_CNT:
        answer = max(answer, bfs(copy.deepcopy(lab)))
        return

    for i in range(y, len(lab)):
        j = 0
        if i == y:
            j = x + 1
        while j < len(lab[i]):
            if lab[i][j] == 0:
                lab[i][j] = 1
                comb(lab, cnt + 1, i, j)
                lab[i][j] = 0
            j += 1


# main #
if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip('\n').split())

    lab = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]
    comb(lab, 0, 0, -1)

    print(answer)
