n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x, y - 1)
        return True
    return False


answer = 0

for row in range(n):
    for column in range(m):
        if dfs(n, m) == True:
            answer += 1

print(answer)
