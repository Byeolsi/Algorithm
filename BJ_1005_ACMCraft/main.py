# 1168 ms

# import
import sys
import collections

# main - 위상 정렬 알고리즘
T = int(sys.stdin.readline().rstrip('\n'))

for t in range(T):
    N, K = map(int, sys.stdin.readline().rstrip('\n').split())
    D = [0] + list(map(int, sys.stdin.readline().rstrip('\n').split()))
    in_degree = [0] * (N + 1) # 진입 차수
    dp = [0] * (N + 1)
    
    matrix = collections.defaultdict(list)
    for k in range(K):
        X, Y = map(int, sys.stdin.readline().rstrip('\n').split())
        matrix[X].append(Y)
        in_degree[Y] += 1
    W = int(sys.stdin.readline().rstrip('\n'))

    q = collections.deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)
            dp[i] = D[i]

    while q:
        cur = q.popleft()
        if cur == W:
            break

        for nxt in matrix[cur]:
            dp[nxt] = max(dp[nxt], dp[cur] + D[nxt])
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                q.append(nxt)

    print(dp[W])
