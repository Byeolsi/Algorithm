# 192 ms

# import #
import sys


# main #
if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip('\n'))
    S = list(map(int, sys.stdin.readline().rstrip('\n').split()))
    Sn = [0 for _ in range(10)]
    answer = 0

    type_n = 0
    left = 0
    for right in range(N):
        if Sn[S[right]] == 0:
            type_n += 1
            if type_n >= 3:
                answer = max(answer, right - left)
                while left < right:
                    Sn[S[left]] -= 1
                    if Sn[S[left]] == 0:
                        type_n -= 1
                        left += 1
                        break
                    left += 1
        Sn[S[right]] += 1

    answer = max(answer, N - left)
    print(answer)
