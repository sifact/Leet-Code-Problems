def reshape(matrix, r, c):
    flat = sum(matrix, [])

    if len(flat) != r * c:
        return matrix

    tuples = zip(*([iter(flat)] * c))

    return map(list, tuples)


def reshape2(matrix, r, c):
    m = len(matrix)

    n = len(matrix[0])

    if r * c != m * n:
        return matrix

    reshaped = [[0] * c for _ in range(r)]

    for i in range(r * c):
        reshaped[i // c][i % c] = matrix[i // n][i % n]
    return reshaped


mat = [list(map(int, input().split())) for i in range(int(input()))]
r1, c1 = int(input()), int(input())
print(reshape2(mat, r1, c1))
