# 44 ms

# import
import sys


# global
memo = {}


# function
def divide_and_conquer(A, B, C):
    if B == 1:
        return A % C
    elif B in memo:
        return memo[B]

    left = B // 2
    result = (divide_and_conquer(A, left, C) * divide_and_conquer(A, B - left, C)) % C
    memo[B] = result

    return result


# main
A, B, C = map(int, sys.stdin.readline().rstrip('\n').split())

print(divide_and_conquer(A, B, C))
