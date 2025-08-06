# 3540 ms

# import #
import sys


# global #
sys.setrecursionlimit(10**6)


# functions #
def dfs(cur, team) -> int:
    # 사이클 발견
    if cur in team:
        return cur
    elif visited[cur]:
        return 0

    visited[cur] = True
    team.add(cur)
    end = dfs(sel_std_no[cur], team)
    if end in team:
        grouped[cur] = True
        team.remove(cur)
        return end
    else:
        team.remove(cur)
        return 0


# main #
T = int(sys.stdin.readline().rstrip('\n'))

for t in range(T):
    n = int(sys.stdin.readline().rstrip('\n'))
    sel_std_no = [0] + list(map(int, sys.stdin.readline().rstrip('\n').split()))
    visited = [False] * (n + 1) # 이미 확인해 본 학생
    grouped = [False] * (n + 1) # 그룹으로 형성된 학생

    for i in range(1, n + 1):
        if visited[i]:
            continue
        dfs(i, set())

    answer = 0
    for i in range(1, n + 1):
        answer += grouped[i] is False

    print(answer)
