# 73점 - 656 ms

# import
import sys


# functions
def dfs(cur):
    global one_cnt
    # global in_out
    # global adj_list
    # global visited

    if in_out[cur] == '1':
        return

    for to in adj_list[cur]:
        if in_out[to] == '1':
            one_cnt += 1
        if visited[to]:
            continue
        visited[to] = True
        dfs(to)


# main
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline().rstrip('\n'))
in_out = ['0'] + list(sys.stdin.readline().rstrip('\n'))

adj_list = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

answer = 0
for i in range(N - 1):
    A, B = map(int, sys.stdin.readline().rstrip('\n').split())
    adj_list[A].append(B)
    adj_list[B].append(A)
    if in_out[A] == '1' and in_out[B] == '1':
        answer += 2

one_cnt = 0
# 0부터 시작해서 dfs 탐색
for i in range(1, N + 1):
    if in_out[i] == '1' or visited[i]:
        continue
    one_cnt = 0
    visited[i] = True
    dfs(i)
    # N * (N - 1) 이 현재 부분 그래프가 가질 수 있는 모든 경우의 수
    answer += one_cnt * (one_cnt - 1)

print(answer)