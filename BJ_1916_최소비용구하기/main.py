# import
import sys
# from queue import PriorityQueue
import heapq


# functions
def dijkstra(cur):
    # pq = PriorityQueue()
    pq = []

    distances[cur] = 0
    # pq.put((distances[cur], cur))
    heapq.heappush(pq, (distances[cur], cur))

    # while pq.qsize() > 0:
    while pq:
        # weight, cur = pq.get()
        weight, cur = heapq.heappop(pq)

        if distances[cur] < weight:
            continue

        for vertex_weight, to in adj_list[cur]:
            vertex_weight += distances[cur]
            if distances[to] > vertex_weight:
                distances[to] = vertex_weight
                # pq.put((vertex_weight, to))
                heapq.heappush(pq, (vertex_weight, to))


# main
N = int(sys.stdin.readline().rstrip('\n'))
M = int(sys.stdin.readline().rstrip('\n'))

adj_list = [[] for _ in range(N + 1)]
# visited = [False for _ in range(N + 1)]
distances = [sys.maxsize for _ in range(N + 1)]
for i in range(M):
    cur, to, weight = map(int, sys.stdin.readline().rstrip('\n').split())
    adj_list[cur].append((weight, to))
A, B = map(int, sys.stdin.readline().rstrip('\n').split())

dijkstra(A)
print(distances[B])
