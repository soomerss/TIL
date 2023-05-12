from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


# 갈 수 있는 한 단계만큼 표시한다. 그러면 우리는 deque를 사용하고, 한 단계만 탐험한다는 것을 알았다.
# 그리고 queue는 한 칸을 미리 뺴놔서 어디로 갈지를 미리 판단한다.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# deque에서
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # 너비로 완전탐색아님??..
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]


print(bfs(0, 0))
