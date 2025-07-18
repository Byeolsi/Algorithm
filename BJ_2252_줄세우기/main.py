# 208 ms

# import
import sys
import collections

# functions
def topology_sort() -> list:
    sorted_list = []
    
    q = collections.deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        sorted_list.append(cur)

        for nxt in matrix[cur]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                q.append(nxt)

    return sorted_list


# main
N, M = map(int, sys.stdin.readline().rstrip('\n').split())

matrix = collections.defaultdict(list)
in_degree = [0] * (N + 1) # 진입 차수
for m in range(M):
    A, B = map(int, sys.stdin.readline().rstrip('\n').split())
    matrix[A].append(B)
    in_degree[B] += 1

sorted_list = topology_sort()
# 싸이클 판별
if len(sorted_list) == N:
    print(' '.join(map(str, sorted_list)))
else:
    print("cycle")
