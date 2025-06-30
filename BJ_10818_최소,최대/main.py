# 388 ms

# import
import sys


# main
N = int(sys.stdin.readline().rstrip('\n'))

nums = list(map(int, sys.stdin.readline().rstrip('\n').split()))

print(min(nums), max(nums))
