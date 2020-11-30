def minPathSum1(grid):
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0:
                continue

            # cases for element in top row
            if r - 1 < 0:
                print('Inside of if')
                grid[r][c] = grid[r][c] + grid[r][c - 1]

            # cases for element in leftmost column
            elif c - 1 < 0:
                print()
                print('Inside of elif')
                grid[r][c] = grid[r][c] + grid[r - 1][c]

            # normal case
            else:
                print()
                print('Inside of else')
                grid[r][c] = grid[r][c] + min(grid[r - 1][c], grid[r][c - 1])
            print(grid)
    print()
    return grid[-1][-1]


def minimumPath(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(1, cols):
        matrix[0][i] = matrix[0][i - 1]

    for j in range(1, rows):
        matrix[j][0] += matrix[j - 1][0]

    for i in range(1, rows):
        for j in range(1, cols):
            matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])

    return matrix[-1][-1]

array = [list(map(int, input().split())) for _ in range(int(input()))]
print(minPathSum1(array))
