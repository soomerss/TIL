from itertools import permutations

n = int(input())
li = list(map(int,input().split()))

per_num = list(permutations(li, n))

results = []

for tuples in per_num:
    result = 0
    for i in range(len(tuples) - 1):
        abs_minus = abs(tuples[i + 1] - tuples[i])
        result += abs_minus
    results.append(result)

print(max(results))
