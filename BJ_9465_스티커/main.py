# 808 ms

# import
import sys


# main
T = int(sys.stdin.readline().rstrip('\n'))

for t in range(T):
    n = int(sys.stdin.readline().rstrip('\n'))
    stickers = [[0] + list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(2)]

    for i in range(2, n + 1):
        stickers[0][i] = max(stickers[0][i - 1], stickers[1][i - 1] + stickers[0][i])
        stickers[1][i] = max(stickers[1][i - 1], stickers[0][i - 1] + stickers[1][i])

    print(max(stickers[0][n], stickers[1][n]))
