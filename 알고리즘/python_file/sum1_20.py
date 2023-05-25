import numpy as np

n, m = map(int, input().split())

first = []
two = []
for i in range(n):
    first.append(list(map(int, input().split())))

for i in range(n):
    two.append(list(map(int, input().split())))

df1 = np.array(first)
df2 = np.array(two)

df3 = df1 + df2
