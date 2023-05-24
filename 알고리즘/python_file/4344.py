c = int(input())
case = []
for i in range(c):
    case.append(list(map(int, input().split())))


def count_and_print(li):
    count = 0
    avg = sum(li[1:]) / li[0]
    for i in li[1:]:
        if i > avg:
            count += 1
    print("{:.3f}%".format(count / li[0] * 100))


for i in case:
    count_and_print(i)
