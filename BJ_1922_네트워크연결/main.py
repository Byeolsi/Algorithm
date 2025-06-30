# 352 ms

# import
import sys
import heapq


# function
# a가 속한 집합의 최상위 요소를 반환
def find(a):
    # a가 최상위 요소인 경우
    if p[a] == a:
        return a

    # a가 속한 집합의 최상위 요소를 DFS를 통해 탐색
    # 탐색하면서 a의 부모를 a가 속한 집합의 최상위 요소로 변경
    p[a] = find(p[a])
    return p[a]


# a가 속한 집합과 b가 속한 집합을 합 연산
def union(a, b):
    # b가 속한 집합의 최상위 요소의 부모를
    # a가 속한 집합의 최상위 요소로 변경
    p[find(b)] = find(a)


# main
answer = 0

N = int(sys.stdin.readline().rstrip('\n'))
M = int(sys.stdin.readline().rstrip('\n'))
pq = []
p = [_ for _ in range(N + 1)]

for m in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip('\n').split())
    heapq.heappush(pq, (c, a, b))

# 우선순위 큐를 사용하여 거리(비용)이 가장 작은 간선을 먼저 추출
while pq:
    c, a, b = heapq.heappop(pq)
    # a와 b의 부모가 같은 경우
    if find(a) == find(b):
        continue
    # a가 속한 집합과 b가 속한 집합을 합 연산
    union(a, b)
    answer += c

print(answer)
