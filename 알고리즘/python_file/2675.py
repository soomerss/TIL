n = int(input())
case = []
for _ in range(n):
    a, b = input().split()
    case.append((int(a), b))

for n, cha in case:
    for i in cha:
        print(i * n, end="")
    print()
