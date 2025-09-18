# 60 ms

# import #
import sys
from collections import deque


# main #
if __name__ == "__main__":
    visited = [False for _ in range(101)]
    N, M = map(int, sys.stdin.readline().rstrip('\n').split())
    teleport = {}

    # 사다리 혹은 뱀의 경로
    for i in range(N + M):
        fr, to = map(int, sys.stdin.readline().rstrip('\n').split())
        teleport[fr] = to

    # BFS 탐색으로 최단 경로 탐색
    q = deque()
    q.append(1)
    depth = 0
    size = len(q)
    while q:
        cur = q.popleft()
        if cur == 100:
            break

        for i in range(1, 7):
            nxt = cur + i
            if nxt > 100:
                break
            if visited[nxt]:
                continue

            # 사다리 혹은 뱀
            # while 문을 사용한 이유는 사다리 혹은 뱀이 연속적으로 놓아져 있는 경우가 있을 수 있기 때
            while nxt in teleport:
                visited[nxt] = True
                nxt = teleport[nxt]
            q.append(nxt)
            visited[nxt] = True

        size -= 1
        if size == 0:
            depth += 1
            size = len(q)

    print(depth)
