case = [int(input()) for i in range(9)]

maximum = max(case)
index = case.index(maximum) + 1

print(maximum)
print(index)
