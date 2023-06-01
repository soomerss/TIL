import collections

n, m = map(int, input().split())

oven = list(map(int, input().split()))
int_d = collections.deque(map(int, input().split()))

index = 0

for i in range(n - 1):
    if oven[i] < oven[i + 1]:
        oven[i + 1] = oven[i]

for i in range(n-1,-1,-1):
    if int_d[index] <= oven[i]:



binary_search(int_d, oven, 0, n - 1)
