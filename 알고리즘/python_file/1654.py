n, m = map(int, input().split())
case = [int(input()) for _ in range(n)]
end = sum(case) // n + 1


def binary_search(end):
    start = 1
    while start < end:
        mid = (start + end) // 2
        count = 0
        for i in case:
            count += i // mid
        check = (start, end)
        if count >= m:
            start = mid
        elif count < m:
            end = mid
        if check == (start, end):
            return start
    return binary_search(end)


print(binary_search(end))
