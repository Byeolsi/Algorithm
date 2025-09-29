# 1040 ms

# import #
import sys


# function
def isBomb(stack, bomb, start):
    for i in range(len(bomb)):
        if stack[start + i] != bomb[i]:
            return False
    return True


# main #
if __name__ == "__main__":
    s = list(sys.stdin.readline().rstrip('\n'))
    bomb = list(sys.stdin.readline().rstrip('\n'))

    stack = []
    for ch in s:
        # 한 글자씩 스택에 추가
        stack += ch
        # 문자열 끝 부분이 폭발 문자열과 같다면 제거(pop)
        while len(stack) >= len(bomb) and isBomb(stack, bomb, len(stack) - len(bomb)):
            for _ in range(len(bomb)):
                stack.pop()

    if stack:
        print(''.join(stack))
    else:
        print("FRULA")
