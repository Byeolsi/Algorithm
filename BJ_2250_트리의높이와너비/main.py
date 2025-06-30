# 92 ms

# import
import sys
from collections import deque


# global
index = 1
answer = 0
answer_depth = 0


# function
def find_root(cur):
    if parents[cur] == cur:
        return cur

    return find_root(parents[cur])


# dfs 탐색하여 왼쪽부터 순서 위치 정의
def dfs(cur):
    global index
    
    if adj_list[cur][0] != -1:  # left child
        dfs(adj_list[cur][0])
        
    location[cur] = index
    index += 1
    
    if adj_list[cur][1] != -1:  # right child
        dfs(adj_list[cur][1])


# bfs 탐색하여 depth마다 맨 왼쪽 위치 노드와 맨 오른쪽 위치 노드의 차이 계산
def bfs(cur):
    global answer
    global answer_depth
    
    q = deque()
    q.append(cur)
    
    min_index = N
    max_index = 1
    depth = 1
    size = len(q)
    while q:
        cur = q.popleft()
        if adj_list[cur][0] != -1:      # left child
            q.append(adj_list[cur][0])
        if adj_list[cur][1] != -1:      # right child
            q.append(adj_list[cur][1])
        min_index = min(min_index, location[cur])
        max_index = max(max_index, location[cur])

        size -= 1
        if size == 0:
            if answer < max_index - min_index + 1:
                answer = max_index - min_index + 1
                answer_depth = depth
            min_index = N
            max_index = 1
            depth += 1
            size = len(q)
            

# main
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline().rstrip('\n'))
location = [None for _ in range(N + 1)]

adj_list = [[] for _ in range(N + 1)]
parents = [_ for _ in range(N + 1)]
for i in range(1, N + 1):
    p, left, right = map(int, sys.stdin.readline().rstrip('\n').split())
    adj_list[p].append(left)
    adj_list[p].append(right)
    if left != -1:
        parents[left] = p
    if right != -1:
        parents[right] = p

root = find_root(1)
dfs(root)
bfs(root)
print(answer_depth, answer)
