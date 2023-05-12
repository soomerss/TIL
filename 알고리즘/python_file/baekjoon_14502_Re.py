import copy
from collections import deque
from itertools import combinations

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

wall = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            wall.append((i, j))

wa = list(combinations(wall, 3))


def bfs(temp, row, col):
    queue = deque()
    queue.append((row, col))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                queue.append((nx, ny))
                temp[nx][ny] = 2
    return temp


answer = []

for i in wa:
    temp = copy.deepcopy(graph)
    count = 0
    for x, y in i:
        temp[x][y] = 1
    for row in range(n):
        for col in range(m):
            if temp[row][col] == 2:
                temp = bfs(temp, row, col)

    for row in range(n):
        for col in range(m):
            if temp[row][col] == 0:
                count += 1
    answer.append(count)

print(max(answer))
