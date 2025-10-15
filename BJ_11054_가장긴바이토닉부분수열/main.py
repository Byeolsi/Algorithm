# 348 ms

# import #
import sys


# main #
if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip('\n'))
    arr = list(map(int, sys.stdin.readline().rstrip('\n').split()))

    ascending = [[arr[_]] for _ in range(N)]    # 가장 긴 증가하는 부분 수열
    descending = [[arr[_]] for _ in range(N)]   # 가장 긴 감소하는 부분 수열

    # 가장 긴 증가하는 부분 수열 구하기
    for i in range(N):
        max_len = 0
        max_arr = []
        for j in range(i):
            if ascending[j][-1] < ascending[i][0] and \
               max_len < len(ascending[j]):
                max_len = len(ascending[j])
                max_arr = ascending[j]
        ascending[i] = max_arr + ascending[i]

    # 가장 긴 감소하는 부분 수열 구하기
    for i in range(N - 1, -1, -1):
        max_len = 0
        max_arr = []
        for j in range(N - 1, i, -1):
            if descending[j][0] < descending[i][-1] and \
               max_len < len(descending[j]):
                max_len = len(descending[j])
                max_arr = descending[j]
        descending[i] = descending[i] + max_arr

    # 두 부분 수열의 길이의 합 중 가장 큰 값 구하기
    answer = 0
    for i in range(N):
        # 중앙 값이 겹치므로, -1
        answer = max(answer, len(ascending[i]) + len(descending[i]) - 1)

    print(answer)
