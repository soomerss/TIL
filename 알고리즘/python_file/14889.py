from itertools import combinations, permutations

n = int(input())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))


all_people = [i for i in range(n)]

start_team = list(combinations(all_people, n // 2))
link_team = []

answer = 999999

for tuples in start_team:
    tmp = set(all_people)
    for j in tuples:
        tmp.remove(j)
    link_team.append(tuple(tmp))

# 각 팀별 2명의 순열과 그 값을 list에 넣고 sum
for i in range(len(start_team)):
    # 순서대로 튜플 뽑기
    start_p = list(permutations(start_team[i], 2))
    link_p = list(permutations(link_team[i], 2))
    start_sum = []
    link_sum = []
    for j in range(len(start_p)):
        start_value = s[start_p[j][0]][start_p[j][1]]
        link_value = s[link_p[j][0]][link_p[j][1]]
        start_sum.append(start_value)
        link_sum.append(link_value)
    if abs(sum(start_sum) - sum(link_sum)) < answer:
        answer = abs(sum(start_sum) - sum(link_sum))

print(answer)
