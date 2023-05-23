number = int(input())

number_memo = dict()


def memo_fibo(n):
    global number_memo
    goal = n
    n = 0
    if n < 0:
        raise Exception("0이상의 정수를 입력해주세요.")
    while n <= goal:
        if n == 0:
            number_memo[0] = 0
        if n == 1:
            number_memo[1] = 1
        if n >= 2:
            number_memo[n] = number_memo[n - 1] + number_memo[n - 2]
        n += 1

    return number_memo[goal]


print(memo_fibo(number))


## 재귀함수로 구현 못함...
