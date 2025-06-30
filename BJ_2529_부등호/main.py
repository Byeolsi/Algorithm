# 44 ms

k = int(input())
ineq_sign = input().split()

# max 값 구하기
numbers = [False for _ in range(10)]
# lst: 가장 먼저 나와야 할 수
lst = 9
max = ""
for i in range(k):
    # i 번째 수 구하기.
    j = i
    cnt = 0
    # 현재 부등호가 "<"이면 cnt를 1 증가시키고, 다음 부등호를 확인
    while j < k and ineq_sign[j] != ">":
        j += 1
        cnt += 1
    # 해당 숫자는 사용하였으므로, True로 변경
    max += str(lst - cnt)
    numbers[lst - cnt] = True
    while numbers[lst]:
        lst -= 1
# 마지막 숫자 추가
max += str(lst)

# min 값 구하기
# max 값 구하는 방법을 반대로
numbers = [False for _ in range(10)]
lst = 0
min = ""
for i in range(k):
    j = i
    cnt = 0
    while j < k and ineq_sign[j] != "<":
        j += 1
        cnt += 1
    numbers[lst + cnt] = True
    min += str(lst + cnt)
    while numbers[lst]:
        lst += 1
min += str(lst)

print(max)
print(min)