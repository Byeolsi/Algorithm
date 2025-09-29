# 636 ms

# import #
import sys
import heapq
from collections import defaultdict


# global #
MAX_COST = 200000 * 1000


# function #
def dijkstra(adj_map: dict, N: int, start: int, end: int) -> int:
    pq = []
    d = [MAX_COST for _ in range(N + 1)]

    heapq.heappush(pq, (0, start))
    d[start] = 0
    while pq:
        cost, cur = heapq.heappop(pq)
        if cost > d[cur]:
            continue
        
        for nxt, cost_nxt in adj_map[cur]:
            cost_nxt += cost
            if cost_nxt < d[nxt]:
                heapq.heappush(pq, (cost_nxt, nxt))
                d[nxt] = cost_nxt
            
    return d[end]


# main #
if __name__ == "__main__":
    N, E = map(int, sys.stdin.readline().rstrip('\n').split())
    adj_map = defaultdict(list)
    for _ in range(E):
        a, b, c = map(int, sys.stdin.readline().rstrip('\n').split())
        adj_map[a].append((b, c))
        adj_map[b].append((a, c))
    v1, v2 = map(int, sys.stdin.readline().rstrip('\n').split())

    # 1 -> v1 -> v2 -> N
    # 1 -> v2 -> v1 -> N
    answer = min(dijkstra(adj_map, N, 1, v1) + dijkstra(adj_map, N, v1, v2) + dijkstra(adj_map, N, v2, N), \
                 dijkstra(adj_map, N, 1, v2) + dijkstra(adj_map, N, v2, v1) + dijkstra(adj_map, N, v1, N))

    # 경로가 없는 경우
    if answer >= MAX_COST:
        print(-1)
    else:
        print(answer)
