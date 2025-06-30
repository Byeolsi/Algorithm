# 68 ms

# import
import sys


# function
def dfs(cur, weight):
    global answer

    length = [0]
    # 모든 자식 노드로 DFS 탐색
    for c, w in adj_list[cur]:
        # 각 루트의 최대 길이 추가
        length.append(dfs(c, w))

    # 각 루트의 길이 정렬
    length.sort()
    # 자식 노드가 하나라도 있었다면
    if len(length) >= 2:
        # 가장 긴 2개의 길이를 합산하여 answer 갱신
        answer = max(answer, length[-1] + length[-2])

    # [부모 노드에서 현재 노드로 이어지는 길이 + 가장 긴 길이] 반환
    return weight + length[-1]


# main
sys.setrecursionlimit(10**6)

answer = 0

n = int(sys.stdin.readline().rstrip('\n'))
adj_list = [[] for _ in range(n + 1)]
for i in range(n - 1):
    P, C, weight = map(int, sys.stdin.readline().rstrip('\n').split())
    adj_list[P].append((C, weight))

dfs(1, 0)

print(answer)
