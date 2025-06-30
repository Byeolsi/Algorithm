# 236 ms

# import
import sys


# function
def dfs(cur, prev, result):
    for vertex in adj_list[cur]:
        # 다음 방문할 노드가 바로 직전 노드라면 continue
        # 예. A -> B, B -> A는 양방향 간선에 의한 경우이기 때문에 고려 X
        if vertex == prev:
            continue
        # 다음 방문할 노드가 이미 방문한 노드라면 현재 그래프는 트리가 아님
        # 일단 방문할 수 있는 노드는 모두 방문하도록 함
        if visited[vertex]:
            result = False
            continue

        # DFS 탐색
        # DFS 탐색하면서 result가 False가 되었다면 트리가 아님
        visited[vertex] = True
        result = dfs(vertex, cur, result)

    return result


# main
t = 1
n, m = map(int, sys.stdin.readline().rstrip('\n').split())
while n != 0 or m != 0:
    answer = 0
    adj_list = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]

    # 양방향 간선 추가
    for i in range(m):
        a, b = map(int, sys.stdin.readline().rstrip('\n').split())
        adj_list[a].append(b)
        adj_list[b].append(a)

    for i in range(1, n + 1):
        # 이미 방문한 노드라면 continue
        if visited[i]:
            continue

        # 아직 방문하지 않는 노드라면 DFS 탐색
        visited[i] = True
        if dfs(i, 0, True):
            answer += 1

    if answer == 0:
        print("Case {}: No trees.".format(t))
    elif answer == 1:
        print("Case {}: There is one tree.".format(t))
    else:
        print("Case {}: A forest of {} trees.".format(t, answer))

    t += 1
    n, m = map(int, sys.stdin.readline().rstrip('\n').split())
