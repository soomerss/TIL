n = int(input())
n_arr = list(map(int, input().split()))
n_arr.sort()
m = int(input())
m_arr = list(map(int, input().split()))


def binary_search(arr, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if arr[mid] == target:
        return 1
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    else:
        return binary_search(arr, target, start, mid - 1)


for i in m_arr:
    print(binary_search(n_arr, i, 0, len(n_arr) - 1))
