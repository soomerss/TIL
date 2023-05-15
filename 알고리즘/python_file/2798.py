from itertools import combinations

n, m = map(int, input().split())
num_arr = list(map(int, input().split()))

com_arr = combinations(num_arr, 3)
sum_arr = []

for i in com_arr:
    sum_arr.append(sum(i))

sum_arr.sort(key=lambda x: abs(m - x))

answer = 0

for i in sum_arr:
    if i > m:
        continue
    answer = i
    break

print(answer)
