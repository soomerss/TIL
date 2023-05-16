n = int(input())
num = list(map(int, input().split()))
target = int(input())

answer_dict = dict()

for i in num:
    answer_dict[i] = answer_dict.get(i, 0) + 1

print(answer_dict[target])
