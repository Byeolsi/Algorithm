# # 단순 반복문(비트마스킹) - 6844 ms
#
# # functions
# # 두 팀의 점수를 계산하여 두 팀의 점수의 차를 반환
# def cal(stats, start_team, link_team):
#     start_team_score = 0
#     for i in range(len(start_team)):
#         prev = start_team[i]
#         for j in range(i + 1, len(start_team)):
#             cur = start_team[j]
#             start_team_score += stats[prev][cur]
#             start_team_score += stats[cur][prev]
#
#     link_team_score = 0
#     for i in range(len(link_team)):
#         prev = link_team[i]
#         for j in range(i + 1, len(link_team)):
#             cur = link_team[j]
#             link_team_score += stats[prev][cur]
#             link_team_score += stats[cur][prev]
#
#     return abs(start_team_score - link_team_score)
#
#
# # main
# N = int(input())
# stats = [list(map(int, input().split())) for _ in range(N)]
#
# answer = 1000000000
# # 2^N까지 1씩 증가
# for selected in range(2 ** N):
#     start_team = []
#     link_team = []
#     for i in range(N):
#         # 비트 한 자리씩 체크해가며, 1인지 확인
#         # 1이라면, start_team에 추가
#         if selected & (2 ** i) > 0:
#             start_team.append(i)
#         # 아니라면, link_team에 추가
#         else:
#             link_team.append(i)
#     # 모두 확인해 본 결과, 정확히 절반으로 팀이 나누어 구성되었다면,
#     if len(start_team) == N / 2:
#         # 두 팀의 점수 차를 확인하고, 답을 갱신
#         result = cal(stats, start_team, link_team)
#         answer = min(answer, result)
#
# print(answer)


##################################################


# 조합(비트마스킹) - 1388 ms

# global
answer = 100000000


# functions
# 두 팀의 점수를 계산하여 두 팀의 점수의 차를 반환
def cal(selected):
    global stats

    # selected에 따라서 두 팀을 나눔
    start_team = []
    link_team = []
    for i in range(N):
        if selected & (1 << i) > 0:
            start_team.append(i)
        else:
            link_team.append(i)

    start_team_score = 0
    for i in range(len(start_team)):
        left = start_team[i]
        for j in range(i + 1, len(start_team)):
            right = start_team[j]
            start_team_score += stats[left][right] + stats[right][left]

    link_team_score = 0
    for i in range(len(link_team)):
        left = link_team[i]
        for j in range(i + 1, len(link_team)):
            right = link_team[j]
            link_team_score += stats[left][right] + stats[right][left]

    return abs(start_team_score - link_team_score)


def comb(cnt, index, selected):
    global N
    global answer

    # 전체 인원의 절반을 선택해야 하므로, cnt가 N / 2가 되었을 때 값을 계산하여 답을 갱신
    if cnt >= N / 2:
        answer = min(answer, cal(selected))
        return

    # 조합은 아래와 형태로 구성
    # visited 리스트를 필요로 하지 않음
    for i in range(index + 1, N):
        comb(cnt + 1, i, selected | (1 << i))


# main
N = int(input())
stats = [list(map(int, input().split())) for _ in range(N)]

comb(0, 0, 0)
print(answer)