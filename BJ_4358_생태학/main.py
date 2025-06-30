# 524 ms

# import
import sys


# main
# 딕셔너리 사용
trees = {}
total = 0
while True:
    tree = sys.stdin.readline().rstrip('\n')
    if tree == "":
        break

    # 해당 종이 딕셔너리에 이미 있는지 확인
    # 없으면 딕셔너리에 새로운 종 추가
    if not tree in trees:
        trees[tree] = 0
    trees[tree] += 1
    total += 1

# key 기준으로 정렬
sorted_trees = sorted(trees.items())
for cur, cnt in sorted_trees:
    print("%s %.4f" % (cur, (cnt / total) * 100))
