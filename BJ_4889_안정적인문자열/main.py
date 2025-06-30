# 48 ms

# import
import sys


# main
t = 0
while True:
    s = sys.stdin.readline().rstrip('\n')
    if '-' in s:
        break
    t += 1

    answer = 0
    cnt = 0
    for ch in list(s):
        # 문자가 '{'이면,
        if ch == '{':
            # 카운트 +1('{' 하나 저장)
            cnt += 1
        # 문자가 '}'이면,
        else:
            # 카운트가 없으면,
            if cnt == 0:
                # 답 +1('}' -> '{')
                answer += 1
                cnt += 1
            # 카운트가 있으면,
            else:
                # 카운트 -1('{' 하나 소모)
                cnt -= 1

    # 카운트가 남아있으면, 정답 +(cnt / 2)(저장해 둔 '{'의 절반을 '}'로 변환)
    answer += cnt // 2
    print("{}. {}".format(t, answer))
