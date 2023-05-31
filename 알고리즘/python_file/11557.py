t = int(input())
for i in range(t):
    n = int(input())
    tmp = {}
    for j in range(n):
        name, number = input().split()
        tmp[name] = int(number)
        a = sorted(tmp.items(), key=lambda x: x[1], reverse=True)
    print(a[0][0])
