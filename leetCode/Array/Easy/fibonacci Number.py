def fib(N):
    if N == 0:
        return 0
    elif N < 3:
        return 1
    return fib(N - 1) + fib(N - 2)


# 2 variables:
def fib2(N):
    a, b = 0, 1
    for _ in range(N):
        print('iter')
        a, b = b, a + b

        print(a, b)
    return a


# memoized recursive:
def fib3(N):
    memo = {}
    if N == 0:
        return 0
    if N == 1:
        return 1

    if N - 1 not in memo:
        memo[N - 1] = fib(N - 1)
    if N - 2 not in memo:
        memo[N - 2] = fib(N - 2)
    # print(memo)

    return memo[N - 1] + memo[N - 2]


n = int(input())
print(fib3(n))



