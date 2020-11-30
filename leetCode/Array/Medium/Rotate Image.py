def rotate(matrix):
    n = len(matrix)

    # transpose
    for i in range(n):
        for j in range(i + 1, n):
            print(i, j)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            print()

    # flip horizontally:
    for i in range(n):
        for j in range(n // 2):
            print(i, j)
            matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]

    return matrix


m = int(input())
array_2D = []
for _ in range(m):
    array_2D.append(list(map(int, input().split())))

print(rotate(array_2D))
