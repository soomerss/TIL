import sys

sys.setrecursionlimit(100000)

r, c = map(int, input().split())
graph = []
for i in range(r):
    graph.append(list(map(lambda a: ord(a) - 65, input())))

check = [0] * 26
check[graph[0][0]] = 1
answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, cnt):
    global answer
    answer = max(answer, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not check[graph[nx][ny]]:
            check[graph[nx][ny]] = 1
            dfs(nx, ny, cnt + 1)
            check[graph[nx][ny]] = 0


dfs(0, 0, 1)
print(answer)
