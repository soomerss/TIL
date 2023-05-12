import sys

sys.setrecursionlimit(100000)

from copy import deepcopy

n = int(input())
graph = []
my_height = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    my_height.append(max(graph[i]))
graph1 = deepcopy(graph)
answer = []


def dfs(x, y, height):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] > height:
        graph[x][y] = 0
        dfs(x - 1, y, height)
        dfs(x + 1, y, height)
        dfs(x, y - 1, height)
        dfs(x, y + 1, height)
        return True
    return False


def count_return(height):
    count = 0
    for row in range(n):
        for column in range(n):
            if dfs(row, column, height) == True:
                count += 1
    return count


for i in range(1, max(my_height) + 1):
    answer.append(count_return(i))
    graph = deepcopy(graph1)


## 아무것도 물에 잠기지 않을 수 있다가 힌트였다..
if max(answer) > 1 :
    print(max(answer))
else :
    print(1)
