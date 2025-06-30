# 112 ms

# statics
dt = [ [ -1, 0 ], [ 0, 1 ], [ 1, 0 ], [ 0, -1 ] ]


# functions
# check 함수
def check(i, j):
    max = 1

    # y축 확인
    cnt = 1
    prev = colors[0][j]
    for y in range(1, len(colors)):
        # 이전 글자와 같다면, cnt += 1
        if colors[y][j] == prev:
            cnt += 1
        # 이전 글자와 다르다면, cnt = 1
        else:
            # max가 cnt보다 작은 경우, max 갱신
            if max < cnt:
                max = cnt
            cnt = 1
            prev = colors[y][j]
    # x 마지막까지 반복한 경우에도 한 번 더 체크
    if max < cnt:
        max = cnt

    # x축 확인
    cnt = 1
    prev = colors[i][0]
    for x in range(1, len(colors[i])):
        # 이전 글자와 같다면, cnt += 1
        if colors[i][x] == prev:
            cnt += 1
        # 이전 글자와 다르다면, cnt = 1
        else:
            # max가 cnt보다 작은 경우, max 갱신
            if max < cnt:
                max = cnt
            cnt = 1
            prev = colors[i][x]
    # x 마지막까지 반복한 경우에도 한 번 더 체크
    if max < cnt:
        max = cnt

    return max

# swap 함수
def swap(i, j, y, x):
    tmp = colors[i][j]
    colors[i][j] = colors[y][x]
    colors[y][x] = tmp


# main
N = int(input())
colors = []
for i in range(N):
    str = input()
    colors.append(list(str))

answer = 1;
for i in range(len(colors)):
    for j in range(len(colors[i])):
        # 위치 변경 전 최대 길이 확인
        result = check(i, j)
        if answer < result:
            answer = result

        # 위, 아래, 왼쪽, 오른쪽과 위치 변경 후 최대 길이 확인
        for dy, dx in dt:
            y = i + dy
            x = j + dx
            # 배열의 범위를 벗어난 경우
            if y < 0 or y >= N or x < 0 or x >= N:
                continue
            # 위치를 변경할 두 글자가 같다면
            if colors[i][j] == colors[y][x]:
                continue
            swap(i, j, y, x)
            result = check(i, j)
            if answer < result:
                answer = result
            swap(i, j, y, x)

print(answer)