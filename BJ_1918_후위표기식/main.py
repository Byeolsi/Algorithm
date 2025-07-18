# 32 ms

import sys

medium = list(sys.stdin.readline().rstrip('\n'))
rear = []

# 우선순위 딕셔너리
prior = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '(': +2,
    ')': -2
}

stack = []
upper = 0
for ch in medium:
    # 알파벳인 경우
    if ch.isalpha():
        rear.append(ch)
    # 괄호인 경우
    elif ch == '(' or ch == ')':
        upper += prior[ch]
    # 사칙연산 기호인 경우
    else:
        # 스택이 비어있는 경우
        if not stack:
            stack.append((ch, prior[ch] + upper))
        # 스택 피크와 비교하여 우선순위가 더 큰 경우
        elif stack[-1][1] < prior[ch] + upper:
            stack.append((ch, prior[ch] + upper))
        # 스택 피크와 비교하여 우선순위가 작거나 같은 경우
        else:
            while stack and stack[-1][1] >= prior[ch] + upper:
                rear.append(stack.pop()[0])
            stack.append((ch, prior[ch] + upper))

# 스택에 남아있는 모든 사칙연산 기호를 후위 표기식에 추가
while stack:
    rear.append(stack.pop()[0])

print(''.join(rear))
