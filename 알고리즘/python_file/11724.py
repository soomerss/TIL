import collections
import sys

sys.setrecursionlimit(100000)

node, link = map(int, sys.stdin.readline().rstrip().split())
graph = collections.defaultdict(list)

for i in range(link):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

## visited 만들기
visited = []

count = 0


def dfs(node):
    visited.append(node)
    for i in graph[node]:
        if i not in visited:
            dfs(i)

for i in range(1, node + 1):
    if i not in visited :
        dfs(i)
        count += 1

print(count)
