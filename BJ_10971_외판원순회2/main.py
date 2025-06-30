# 440 ms

# global
min = 20000000


# functions
def perm(cnt, index, sum):
    global min
    # global weights
    # global visited
    # global N

    if cnt == N and weights[index][0] != 0:
        # 시작 지점인 0으로 다시 돌아와야 한다.
        if min > sum + weights[index][0]:
            min = sum + weights[index][0]
        return

    for i in range(N):
        if visited[i]: continue
        if weights[index][i] == 0: continue
        visited[i] = True
        perm(cnt + 1, i, sum + weights[index][i])
        visited[i] = False


# main
N = int(input())
weights = []
for i in range(N):
    weight = list(map(int, input().split(' ')))
    weights.append(weight)

visited = [False for _ in range(N)]
# 외판원 순회는 반드시 다시 원점으로 돌아와야 하기 때문에
# 결국 어느 지점부터 시작하든 결과는 같다.
# 여기서는 0 지점부터 시작했다.
visited[0] = True
perm(1, 0, 0)
print(min)
