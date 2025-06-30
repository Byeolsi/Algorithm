# 1372 ms

# functions
def perm(cnt, perm_list):
    global N

    if cnt >= M:
        print(' '.join(map(str, perm_list)))
        return

    # 중복을 허용하는 중복 순열이므로, visited를 사용할 필요가 없음
    for i in range(1, N + 1):
        perm_list.append(i)
        perm(cnt + 1, perm_list)
        perm_list.pop()


# main
N, M = map(int, input().split())

perm(0, [])