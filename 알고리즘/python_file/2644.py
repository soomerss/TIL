import collections

graph = collections.defaultdict(list)

p_num = int(input())
x, y = map(int, input().split())
g_num = int(input())
for i in range(g_num):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)

count = 0

def dfs():
    target_x = x
    target_y = y
    if target_y in graph[target_x]:
        count += 1
        return
    