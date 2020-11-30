# Top down - TLE:
def climbStairs1(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climbStairs1(n - 1) + climbStairs1(n - 2)


# Bottom up, O(n) space:
def climbingStairs2(n):
    if n == 1:
        return 1

    res = [0 for i in range(n)]
    res[0], res[1] = 1, 2

    for i in range(2, n):
        res[i] = res[i - 1] + res[i - 2]
    return res[-1]


