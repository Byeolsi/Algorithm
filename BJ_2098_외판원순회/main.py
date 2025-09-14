# 988 ms

# import #
import sys


# global #
INF = 16 * 10 ** 6 + 1


# function #
def dfs(cur: int, visited: int) -> int:
    if visited == (1 << N) - 1:     # 모든 도시를 방문했다면
        if graph[cur][0]:           # 출발점으로 가는 경로가 있을 때
            return graph[cur][0]
        else:                       # 출발점으로 가는 경로가 없을 때
            return INF

    if dp[cur][visited] != -1:      # 이미 최소 비용이 계산되어 있다면
        return dp[cur][visited]

    dp[cur][visited] = INF          # 현재 방문한 도시이기에 -1 -> INF
    for nxt in range(1, N):         # 모든 도시를 탐방
        if not graph[cur][nxt]:     # 가는 경로가 없다면 skip
            continue
        if visited & (1 << nxt):    # 이미 방문한 도시라면 skip
            continue

        dp[cur][visited] = min(dp[cur][visited], dfs(nxt, visited | (1 << nxt)) + graph[cur][nxt])
    
    return dp[cur][visited]


# main #
if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip('\n'))
    graph = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]
    dp = [[-1] * (1 << N) for _ in range(N)]

    print(dfs(0, 1))
