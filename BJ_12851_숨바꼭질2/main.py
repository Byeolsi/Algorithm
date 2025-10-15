# 104 ms

# import #
import sys
from collections import deque


# global
MAX = 100000


# function #
def solve(start, end):
    # time[x]: x 위치에 도달하는 최소 시간. -1이면 아직 도달 안 함
    time = [-1] * (MAX + 1)
    # ways[x]: x 위치에 최소 시간으로 도달하는 방법의 수
    ways = [0] * (MAX + 1)

    queue = deque()
    queue.append(N)
    time[N] = 0
    ways[N] = 1

    while queue:
        x = queue.popleft()
        t = time[x]

        for nx in (x - 1, x + 1, x * 2):
            if nx < 0 or nx > MAX:
                continue
            # 아직 방문하지 않은 경우
            if time[nx] == -1:
                time[nx] = t + 1
                ways[nx] = ways[x]
                queue.append(nx)
            # 이미 방문했지만, 같은 최소 시간으로 도달하는 경로가 또 등장한 경우
            elif time[nx] == t + 1:
                ways[nx] += ways[x]

    return (time[end], ways[end])

        
# main #
if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().rstrip('\n').split())
    
    print(*solve(N, K))
