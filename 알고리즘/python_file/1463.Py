import sys

cache = {}
for num in range(1, 10**6 + 1):
    cache[num] = 10000000

cache[1] = 0
for num in range(1, 10**6 + 1):
    if num + 1 <= 10**6:
        cache[num + 1] = min(cache[num + 1], cache[num] + 1)
    if num * 2 <= 10**6:
        cache[num * 2] = min(cache[num * 2], cache[num] + 1)
    if num * 3 <= 10**6:
        cache[num * 3] = min(cache[num * 3], cache[num] + 1)


sys.stdout.write(str(cache[int(input())]))
