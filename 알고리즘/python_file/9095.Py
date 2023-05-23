n = int(input())
test_case = []
for _ in range(n):
    tmp = int(input())
    test_case.append(tmp)


answer = 0


def dfs(count, n):
    global answer
    if count == n:
        answer += 1
        return
    elif count > n:
        return

    dfs(count + 1, n)
    dfs(count + 2, n)
    dfs(count + 3, n)
    return


for i in range(n):
    dfs(0, test_case[i])
    print(answer)
    answer = 0

## elif를 생각하지 못했어 Recursion오류가 계속남 왜냐하면 n을 넘어가는 순간부터 계속 더하기 때문
## global안써서 변수 오류 생성
