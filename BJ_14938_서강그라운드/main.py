# 64 ms

# import #
import sys
import heapq
from collections import defaultdict


# function #
def bfs(start: int, m: int, items: list, adj_map: dict) -> int:
    # 최대 힙을 사용하는 이유:
    # 최대한 적은 거리로 수색하는 경우, 더 많은 수색 범위가 남아 더 많은 구역을 수색할 수 있기 때문
    pq = []
    left_m = [-1 for _ in range(len(items) + 1)]
    added = set()

    result = 0
    heapq.heappush(pq, (-m, start))
    left_m[start] = m
    while pq:
        m, cur = heapq.heappop(pq)
        m *= -1
        # 남은 수색 범위가 갱신되는 경우, 한 번 더 더하는 것을 방지
        if not cur in added:
            result += items[cur]
            added.add(cur)

        if left_m[cur] > m:
            continue
        
        for nxt, nxt_m in adj_map[cur]:
            # 수색 범위에 닿지 않음
            if m - nxt_m < 0:
                continue
            if left_m[nxt] < m - nxt_m:
                heapq.heappush(pq, (-(m - nxt_m), nxt))
                left_m[nxt] = m - nxt_m

    return result


# main #
if __name__ == "__main__":
    n, m, r = map(int, sys.stdin.readline().rstrip('\n').split())
    items = [0] + list(map(int, sys.stdin.readline().rstrip('\n').split()))
    adj_map = defaultdict(list)
    for _ in range(r):
        a, b, l = map(int, sys.stdin.readline().rstrip('\n').split())
        adj_map[a].append((b, l))
        adj_map[b].append((a, l))

    answer = 0
    for start in range(1, n + 1):
        answer = max(answer, bfs(start, m, items, adj_map))

    print(answer)
