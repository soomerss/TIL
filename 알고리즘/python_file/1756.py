from collections import deque

d, n = map(int, input().split())
oven = list(map(int, input().split()))
case = list(map(int, input().split()))

case = deque(case)

answer = d

for i in range(len(oven) - 1):
    if oven[i] < oven[i + 1]:
        oven[i + 1] = oven[i]

for i in range(d - 1, -1, -1):
    if oven[i] >= case[0]:
        case.popleft()
        answer = i + 1

    if not case:
        break

if case:
    print(0)
else:
    print(answer)
