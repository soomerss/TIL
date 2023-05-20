import sys

x = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
answer = 0
for i in range(n):
    value, count = map(int,sys.stdin.readline().rstrip().split())
    answer += value*count

if answer == int(x):
    print('Yes')
else:
    print('No')
