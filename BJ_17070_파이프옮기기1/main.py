# 36 ms

# import #
import sys


# main #
if __name__ == "__main__":
    dt = [[0, -1], [-1, -1], [-1, 0]]
    N = int(sys.stdin.readline().rstrip('\n'))
    house_map = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]
    dp = [[[0 for ___ in range(N)] for __ in range(N)] for _ in range(3)]
    dp[0][0][1] = 1

    for i in range(N):
        for j in range(N):
            # 파이프 끝 위치가 벽인 경우
            if house_map[i][j] == 1:
                continue
            for k in range(len(dt)):
                dy, dx = dt[k]
                ry, rx = i + dy, j + dx
                if ry < 0 or rx < 0:
                    continue
                # 파이프 시작 위치가 벽인 경우
                if house_map[ry][rx] == 1:
                    continue

                if k == 0:
                    dp[k][i][j] += dp[0][ry][rx] + dp[1][ry][rx]
                elif k == 1:
                    # 파이프가 벽을 긁을 경우(대각선)
                    if house_map[ry][j] == 1 or house_map[i][rx] == 1:
                        continue
                    dp[k][i][j] += dp[0][ry][rx] + dp[1][ry][rx] + dp[2][ry][rx]
                else:
                    dp[k][i][j] += dp[1][ry][rx] + dp[2][ry][rx]

    print(dp[0][-1][-1] + dp[1][-1][-1] + dp[2][-1][-1])
