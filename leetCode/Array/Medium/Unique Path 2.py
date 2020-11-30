# Dynamic programming, 0(m * n) space:
def uniquePathWithObstacles1(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    dp = [[0 for _ in range(n)] for _ in range(m)]
    print(dp)
    print()

    for c in range(n):
        if obstacleGrid[0][c] == 1:
            break
        dp[0][c] = 1
    print(dp)
    print()

    for r in range(m):
        if obstacleGrid[r][0] == 1:
            break
        dp[r][0] = 1
    print(dp)
    print()

    for r in range(1, m):
        for c in range(1, n):
            if obstacleGrid[r][c] == 1:
                dp[r][c] = 0
                print('Inside of if')
                print(dp)
                print()
            else:
                print('Inside of else')
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
                print(dp)

    print()
    print(dp)
    return dp[-1][-1]


obstacle_grid = []
for _ in range(int(input())):
    obstacle_grid.append(list(map(int, input().split())))
print(uniquePathWithObstacles1(obstacle_grid))
