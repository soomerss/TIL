n, m = map(int, input().split())

if 45 <= m < 60:
    print(n, m - 45)
else:
    if n - 1 < 0:
        print(23, 60 - (45 - m))
    else:
        print(n - 1, 60 - (45 - m))
