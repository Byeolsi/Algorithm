# 7104 ms

# import #
import sys


# main #
n = int(sys.stdin.readline().rstrip('\n'))
arr = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(n)]

ab, cd = [], []
for i in range(n):
    for j in range(n):
        ab.append(arr[i][0] + arr[j][1])
        cd.append(arr[i][2] + arr[j][3])

ab.sort()
cd.sort()

answer = 0
left, right = 0, len(cd) - 1
while left < len(ab) and right >= 0:
    result = ab[left] + cd[right]
    if result < 0:
        left += 1
    elif result > 0:
        right -= 1
    else:
        nxt_left, nxt_right = left + 1, right - 1
        # 중복되는 숫자의 수(ab) * 중복되는 숫자의 수(cd)
        while nxt_left < len(ab) and ab[left] == ab[nxt_left]:
            nxt_left += 1
        while nxt_right >= 0 and cd[right] == cd[nxt_right]:
            nxt_right -= 1

        answer += (nxt_left - left) * (right - nxt_right)
        left, right = nxt_left, nxt_right

print(answer)
