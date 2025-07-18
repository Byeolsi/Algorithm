# import
import sys
import collections

# global
INF = int(1e9)

# functions
def bellman_ford(start: int) -> bool:
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    # 전체 v - 1번의 라운드(round)를 반복
    for k in range(N):
        # 매 반복마다 '모든 간선'을 확인
        for cur, nxt, cost in edges:
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[nxt] > distance[cur] + cost:
                distance[nxt] = distance[cur] + cost
                # v번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if k == N - 1:
                    return True                

    return False


# main
TC = int(sys.stdin.readline().rstrip('\n'))

for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline().rstrip('\n').split())

    distance = [INF] * (N + 1)
    edges = []

    for __ in range(M):
        S, E, T = map(int, sys.stdin.readline().rstrip('\n').split())
        edges.append((S, E, T))
        edges.append((E, S, T))

    for __ in range(W):
        S, E, T = map(int, sys.stdin.readline().rstrip('\n').split())
        edges.append((S, E, -T))

    # 벨만-포드 알고리즘 수행
    negative_cycle = bellman_ford(1)

    if negative_cycle:
        print("YES")
    else:
        print("NO")
