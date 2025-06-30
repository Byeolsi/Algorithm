# 152 ms - 다익스트라

# import
import sys
import heapq

# main
N, K = map(int, sys.stdin.readline().rstrip('\n').split())

dist = {}

pq = []
heapq.heappush(pq, (0, N))
dist[N] = 0

# N이 K보다 더 큰 경우, -1 씩 걷는 수 밖에 없음
if N >= K:
    print(N - K)
# 다익스트라 알고리
else:
    while pq:
        time, cur = heapq.heappop(pq)
        if cur == K:
            print(time)
            break

        for nxt in (cur - 1, cur + 1, 2 * cur):
            if 0 > nxt or nxt > 100000:
                continue
            nxt_time = time + (nxt != 2 * cur)
            if not nxt in dist or nxt_time < dist[nxt]:
                dist[nxt] = nxt_time
                if nxt != 0:
                    heapq.heappush(pq, (nxt_time, nxt))
