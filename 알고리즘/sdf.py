a = [
    ["R", "R", "R", "B", "B"],
    ["G", "G", "B", "B", "B"],
    ["B", "B", "B", "R", "R"],
    ["B", "B", "R", "R", "R"],
    ["R", "R", "R", "R", "R"],
]

print(a)

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == 'G':
            a[i][j] = 'R'
    
print(a[1])
