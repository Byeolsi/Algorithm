# 304 ms

# import
import sys


# function
def find(a):
    # 최상위 집합 요소 반환
    if sets[a] == a:
        return a

    # 최상위 집합 요소로 단순화
    sets[a] = find(sets[a])
    return sets[a]


def union(a, b):
    # a에 b를 더함(b가 a를 가리킴)
    sets[find(b)] = find(a)


# main
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().rstrip('\n').split())
sets = [_ for _ in range(N + 1)]

for m in range(M):
    com, a, b = map(int, sys.stdin.readline().rstrip('\n').split())
    if com == 0:
        union(a, b)
    else:
        # a와 b의 최상위 집합 요소가 같은 지 확인
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
