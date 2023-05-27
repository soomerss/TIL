n = int(input())


def counts(a, b):
    tmp_list = list()
    count = 1
    while True:
        tmp_len = len(tmp_list)
        tmp = (a**count) % 10
        if tmp not in tmp_list:
            tmp_list.append(tmp)
        if tmp_len == len(tmp_list):
            break
        count += 1

    answer = (b - 1) % len(tmp_list)
    if tmp_list[answer] == 0:
        print(10)
    else:
        print(tmp_list[answer])


for i in range(n):
    x, y = map(int, input().split())
    counts(x, y)
