memo = {1: 1, 2: 2}


def dfs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        if n in memo:
            return memo[n]
        elif n - 1 in memo and n - 2 in memo:
            memo[n] = memo[n - 1] + memo[n - 2]
            return memo[n]
        else:
            return dfs(n - 2) + dfs(n - 1)


for i in range(1, 1001):
    print(dfs(i) % 10007)
