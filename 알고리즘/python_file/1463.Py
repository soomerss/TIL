import sys

sys.setrecursionlimit(10**6)

number = int(sys.stdin.readline().rstrip())

minimum = 999999


def dfs(n, goal, depth):
    global minimum
    if depth > minimum:
        return
    if n > goal:
        return
    if n == goal:
        minimum = min(minimum, depth)

    dfs(n * 3, goal, depth + 1)
    dfs(n * 2, goal, depth + 1)
    dfs(n + 1, goal, depth + 1)
    return


dfs(1, number, 0)
print(minimum)
