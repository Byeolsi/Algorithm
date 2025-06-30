# 56 ms

# import
import sys


# main
string = list(sys.stdin.readline().rstrip('\n'))

# 문자열에서 앞에 문자를 하나씩 빼가면서 팰린드롬인 것을 찾는다.
# 찾는 순간, 빼왔던 문자들을 반대로 뒤에 붙였다고 가정하고 계산 결과를 출력한다.
for i in range(len(string)):
    if string[i:] == string[i:][::-1]:
        break

print(len(string) + i)
