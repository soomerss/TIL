case_len = int(input())
case = []
case_meta = []
for i in range(case_len):
    tmp = []
    x, y, count = map(int, input().split())
    case_meta.append((x,y))
    for j in range(x):
        x_list = [0] * y
        tmp.append(x_list)

    for _ in range(count):
        a, b = map(int, input().split())
        tmp[a][b] = 1

    case.append(tmp)
print(case[0])

def dfs(grpah,meta):
    x = meta[0]
    y = meta[1]
    for i in range(x):
        for j in range(y):
            if grpah[i][j] == 1:
