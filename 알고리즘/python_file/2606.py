import collections

n = int(input())
m = int(input())
graph = collections.defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [-1] * (n + 1)
visited[1] = 1

count = 0


def dfs(n):
    global count
    count += 1
    for i in graph[n]:
        if visited[i] == -1:
            visited[i] = 1
            dfs(i)


dfs(1)
print(count - 1)
