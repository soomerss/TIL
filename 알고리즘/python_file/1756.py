import collections

n, m = map(int, input().split())

oven = list(map(int, input().split()))
int_d = collections.deque(map(int, input().split()))

for i in range(n - 1):
    if oven[i] < oven[i + 1]:
        oven[i + 1] = oven[i]


def binary_search(int_d, oven, start, end):
    while int_d:
        answer = 0
        check = 0
        start = 0
        end = len(oven) - 1
        block = int_d.popleft()
        while start < end:
            mid = (start + end) // 2
            if oven[mid] == block:
                oven = oven[0:mid]
                check += 1
                answer = mid
            elif oven[mid] < block:
                end = mid - 1
            else:
                start = mid + 1
        if check == m:
            print(answer)
    print(0)


binary_search(int_d, oven, 0, n - 1)
