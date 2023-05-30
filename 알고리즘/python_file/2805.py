n, m = map(int,input().split())
case = list(map(int,input().split()))

answer = 0

def binary_s(case,target,start,end):
    global answer
    while start <= end :
        total = 0
        mid = (start + end) // 2
        for i in case:
            if i - mid >= 0:
                total += (i - mid)
        if total >= target:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
binary_s(case,m,0,max(case))
print(answer)
        
    