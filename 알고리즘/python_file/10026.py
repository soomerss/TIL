import sys

sys.setrecursionlimit(100000)

import copy

n = int(input())
graph = [list(map(str, input())) for i in range(n)]
graph1 = copy.deepcopy(graph)
for i in range(len(graph1)):
    for j in range(len(graph1[i])):
        if graph1[i][j] == "G":
            graph1[i][j] = "R"
answer = []
key = ""
count = 0


def dfs(x, y):
    global key
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] != 0 and key == "":
        key = graph[x][y]
    if graph[x][y] == key:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


def dfs1(x, y):
    global key
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph1[x][y] != 0 and key == "":
        key = graph1[x][y]
    if graph1[x][y] == key:
        graph1[x][y] = 0
        dfs1(x - 1, y)
        dfs1(x + 1, y)
        dfs1(x, y - 1)
        dfs1(x, y + 1)
        return True
    return False


for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            count += 1
            key = ""

answer.append(count)

count = 0
key = ""
for i in range(n):
    for j in range(n):
        if dfs1(i, j) == True:
            count += 1
            key = ""

answer.append(count)

print(answer[0], answer[1])
