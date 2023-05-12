n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

mega_house_count = 0
house_list = []
house_count = 0


def bfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] == 1:
        global house_count
        graph[x][y] = 0
        house_count += 1
        bfs(x - 1, y)
        bfs(x + 1, y)
        bfs(x, y - 1)
        bfs(x, y + 1)
        return True
    return False


for row in range(n):
    for column in range(n):
        if bfs(row, column) == True:
            mega_house_count += 1
            house_list.append(house_count)
            house_count = 0

print(mega_house_count)
for i in sorted(house_list):
    print(i)
