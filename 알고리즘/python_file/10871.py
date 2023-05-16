import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))

answer = []

for i in num:
    if i < x:
        answer.append(i)


print(*answer)
