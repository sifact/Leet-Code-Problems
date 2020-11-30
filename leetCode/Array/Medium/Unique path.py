# dp solution:
def uniquePath1(m, n):
    if not m or not n:
        return 0

    dp = [[1] * n] * m
    print(dp)
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            print(dp[i][j])
    print(dp)
    return dp[-1][-1]


# iterative solution:
def uniquePaths2(m, n):
    if not m or not n:
        return 0
    cur = [1] * n
    print(cur)
    for i in range(1, m):
        for j in range(1, n):
            cur[j] = cur[j] + cur[j - 1]
            print(cur[j])
        print(cur)
    return cur[-1]


m1, n1 = int(input()), int(input())
print(uniquePath1(m1, n1))
